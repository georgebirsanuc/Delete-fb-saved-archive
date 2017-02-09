:: - firefox geckodirver required
::   download and add the path to it in PATH enviroment variable
:: - python and pip required
:: - make sure to have the .bat and .py file in the same folder
:: - use Ctrl+C to stop the script
:: -------------------------------------------------------------------
pip install selenium

:pro_loop

python "facebook archived saves removal.py"

GOTO :pro_loop

pause