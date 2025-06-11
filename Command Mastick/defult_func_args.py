# bar is optional and defaults to [] if not specified
# bar.append("baz")    # but this line could be problematic, as we'll see...
def foo(bar=[]):
    bar.append('bar')
    return bar


foo()
foo()
foo()
print(foo())
