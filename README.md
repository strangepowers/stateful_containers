Repo to demontrate the statefulness of containers. I was recently confused by this as a container as I was playing with seemed to be wiping state between restarts  ¯\\\_(ツ)\_/¯ .

From prior docker experience, I thought that containers were stateful but I wanted to be sure as a sanity check.

There is a basic python script `python-test/create_files.py` that creates a file `1.txt` and every second thereafter creates a new file `<inc_num>.txt` (ie, `2.txt`, then `3.txt` etc).

If containers are stateless, then I would expect the directory would be empty and the script would start at `1.txt` again when restarting the container. If stateful, then the script should pick up at the highest number and create new files from this number.

## INSTRUCTIONS

In docker-test: `docker build  .  -t ubuntu_python`

Then, in python-test: `docker build . -t py-script` 

In any directory (with `docker` in the $PATH): `docker run --name py-fun  py-script`. 

This creates a container with a name of `py-fun`, you can check this with `docker ps`, you should see something like this:

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
eeaa42fce560        py-script           "python create_files…"   9 seconds ago       Up 9 seconds                            py-fun
```

You can now go into the container and see all the new files being created:

```
$ docker exec -it py-fun ls
1.txt  2.txt  3.txt  4.txt  create_files.py
```

Now restart `py-fun`:

``` $ docker restart py-fun
py-fun
$ docker exec -it py-fun ls
1.txt	12.txt	15.txt	18.txt	3.txt  6.txt  9.txt
10.txt	13.txt	16.txt	19.txt	4.txt  7.txt  create_files.py
11.txt	14.txt	17.txt	2.txt	5.txt  8.txt
```


```
$ docker restart py-fun
py-fun
$ docker exec -it py-fun ls
1.txt	14.txt	19.txt	23.txt	28.txt	32.txt	4.txt  9.txt
10.txt	15.txt	2.txt	24.txt	29.txt	33.txt	5.txt  create_files.py
11.txt	16.txt	20.txt	25.txt	3.txt	34.txt	6.txt
12.txt	17.txt	21.txt	26.txt	30.txt	35.txt	7.txt
13.txt	18.txt	22.txt	27.txt	31.txt	36.txt	8.txt
```


If the containers are stateless, it should pick off from the snapshotted image every time the container is started, but the `txt` files that were created previously are still present.

On the other hand , if we re-run the image:

`$ docker run --name py-fun2  py-script`

And check the new container:

```
$ docker exec -it py-fun2 ls
1.txt  2.txt  3.txt  4.txt  5.txt  create_files.py
```

It clearly starts off at the snapshotted state from the image.

You can also use `docker commit`, a very handly docker command I've picked up in the past few weeks as described here: https://stackoverflow.com/a/49204476 , to demonstrate the same thing.
