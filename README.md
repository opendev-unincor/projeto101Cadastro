
## projeto de cadastro utilizando django framework  

## INSTALACAO DO PROJETO #
$ git clone git@github.com:opendev-unincor/projeto101Cadastro.git  
$ cd projeto101Cadastro  

## CASO NECCESSITE DE INSTALAR O VIRTUALENV PARA PYTHON 3.6
$ virtualenv enviroment -p python3.6  
### django 2.2 nao funciona sem o python 3.6
   

## ATIVACAO DO VIRTUALENV  
$ source enviroment/bin/activate  
 
## COLOCANDO O DJANGO PRA RODAR  
$ cd projeto101Cadastro  
$ manage.py makemigrations  
$ manage.py migrate  
$ manage.py createsuperuser  
$ manage.py runserver  

## UTILIZAR O ARQUIVO 'settings_local.py' para alterar as configuraçoes  
## NAO deletar o arquivo 'settings_local.py.example'
