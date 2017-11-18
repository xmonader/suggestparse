# suggestparse
argparse extension to allow command suggestions for invalid commands


## Example
```python
def test():
    parser = SuggestingArgumentParser()
    parser.add_argument('--add', '-a', help='add')
    parser.add_argument('--edit', '-e', help='edit')
    parser.add_argument('--delete', '-d', help='delete')
    parser.add_argument('--view', '-v', help='view')
    print(parser.parse_args())

if __name__ == '__main__':
    test()
```

So if you type `--vew` by accident or things like `git comit` or `git clon` you will see something like that.
```
$ python3 suggestparse.py --vew                                                                      
Did you mean:  ['--view']
usage: suggestparse.py [-h] [--add ADD] [--edit EDIT] [--delete DELETE]
                       [--view VIEW]
suggestparse.py: error: unrecognized arguments: --vew
```