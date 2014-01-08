Description
============
Script automaticlly finding place of Invoke or _ATL_EVENT_ENTRY array initialization in code, what's generally one of first thing You should do analizing BHO.


Example of usage session:
=========================
```
Searching for DISPID_BEFORENAVIGATE2
Searching for DISPID_DOCUMENTCOMPLETE
Searching for DISPID_NAVIGATECOMPLETE2
Searching for DISPID_ONQUIT
Potential Invoke function 0x20003b22 : appearance 1
Potential Invoke function 0x20013043 : appearance 1
Potential Invoke function 0x200044cc : appearance 1
Potential Invoke function 0x2000480a : appearance 4
Potential Invoke function 0x20004eec : appearance 1
Potential Invoke function 0x200074f1 : appearance 1
Potential Invoke function 0x2000b093 : appearance 1
Potential Invoke function 0x200022fa : appearance 1
Suggested address of Invoke function : 0x2000480a

```
Bho.py has one more useful functionality, namely **bho_invoke(ea)** function:
```
Python>bho_invoke(0x2000480a)
Found DISPID_NAVIGATECOMPLETE2 at: 200048bb
Found DISPID_NAVIGATEANDFIND at: 200048d0
Found DISPID_PROGRESSCHANGE at: 20004825
Found DISPID_DOCUMENTCOMPLETE at: 20004904
Found DISPID_BEFORENAVIGATE2 at: 200048c6
Found DISPID_ONQUIT at: 200049d7
Found DISPID_DOWNLOADCOMPLETE at: 2000481c
Found DISPID_ISSUBSCRIBED at: 200048d0
```

More info
=========
How to reverse BHO and bho.py script in action You will find here: http://www.icewall.pl/?p=622&lang=en

Enjoy