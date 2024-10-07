httpdbg is a tool for Python developers to easily debug the HTTP(S) client requests in a Python program.

To use it, execute your program using the pyhttpdbg command instead of python and that's it. Open a browser to http://localhost:4909 to view the requests:

![image](https://github.com/user-attachments/assets/417bc889-c55d-48e6-8b7d-035d3802748f)

installation

    pip install httpdbg

usage

interactive console
Open an interactive console using the command pyhttpdbg.

    (venv) dev@host:~/dir$ pyhttpdbg 
    .... - - .--. -.. -... --. .... - - .--. -.. -... --. .... - - .--. -.. -... --.
      httpdbg - HTTP(S) requests available at http://localhost:4909/
    .... - - .--. -.. -... --. .... - - .--. -.. -... --. .... - - .--. -.. -... --.
    Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>

Perform HTTP requests.

You can inspect the HTTP requests directly in your web browser at http://localhost:4909.

script
You can trace all the HTTP requests performed by a script

    pyhttpdbg --script filename.py [arg1 --arg2 ...]
    
pytest
You can trace all the HTTP requests performed during your tests

    pyhttpdbg -m pytest [arg1 --arg2 ...]


If you use the pytest-xdist plugin to execute your tests in parallel, then you must install the pytest-httpdbg plugin if you want to trace the requests done by the pytest workers.

pip install httpdbg[pytest]
module
You can trace all the HTTP requests performed by a library module run as a script using the -m command line argument.

For example, you can view which HTTP requests are performed by pip when you install a package.

pyhttpdbg -m pip install hookdns --upgrade
Initiators
An initiator is the function/method that is at the origin of the HTTP requests. By default, we already support some packages but you can add your own initiators.

To add a new package in the list of initiators, you can use the -i command line argument:

pyhttpdbg -i api_client_pck --script my_script.py
You can use any package as an initiator, this is not limited to HTTP requests.
