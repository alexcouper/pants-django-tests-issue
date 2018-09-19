A minimal repro repo for the problem described
[here](https://github.com/pantsbuild/pants/issues/6526)


To see the issue, run:

```
./pants test src/python/project1:tests src/python/project2:tests
```

Note that both of these commands pass:

```
./pants test src/python/project1:tests
./pants test src/python/project2:tests 
```

As do both of these:

```
PYTHONPATH=$(pwd)/src/python pytest src/python/project1
PYTHONPATH=$(pwd)/src/python pytest src/python/project2
```