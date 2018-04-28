# samdi-get
A simple Python script to get reported debris data from http://www.marinedebris.engr.uga.edu/

```
                                     _
                                    (_)
              |    .
          .   |L  /|   .          _
      _ . |\ _| \--+._/| .       (_)
     / ||\| Y J  )   / |/| ./
    J  |)'( |        ` F`.'/        _
  -<|  F         __     .-<        (_)
    | /       .-'. `.  /-. L___       
    J \      <    \  | | O\|.-'  _   
  _J \  .-    \/ O | | \  |F    (_) 
 '-F  -<_.     \   .-'  `-' L__    
__J  _   _.     >-'  )._.   |-'  
`-|.'   /_.           \_|   F    
  /.-   .                _.<     
 /'    /.'             .'  `\    
  /L  /'   |/      _.-'-\
 /'J       ___.---'\|
   |\  .--' V  | `. `
   |/`. `-.     `._)
      / .-.\
VK    \ (  `\
       `.\

```
Make sure your venv is ready, from within the project's folder:

```
$ easy_install virtualenv
$ mkdir ./virtualenvs
$ virtualenv ./virtualenvs/samdi
```

Activate and install reqs:

```
$ source virtualenvs/samdi/Scripts/activate
$ pip install -r requirements.txt
```

Usage:
```
$ python main.py 1-1-2018 4-1-2018 ./output.csv
```

Note: input dates expected to be in `%m-%d-%Y` format.