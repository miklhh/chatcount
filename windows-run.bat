@ECHO OFF
FOR /F "tokens=* USEBACKQ" %%F IN (`dir /b facebook-*.zip`) DO ( SET arg=%%F )
python chatcount.py %arg%
PAUSE