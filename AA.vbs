Dim venvPath, scriptPath, argPath, shell

' Define the virtual environment and script paths directly in the script
venvPath = "D:\Grad\OCR-RPA\.venv"  ' Change this to your virtual environment path
scriptPath = "D:\Grad\OCR-RPA\Uipath_driver_code.py"  ' Change this to your script path

' Check if the user provided the argument path
If WScript.Arguments.Count < 1 Then
    WScript.Echo "Usage: cscript run_script.vbs <arg_path>"
    WScript.Quit 1
End If

' Get the argument path from command line argument
argPath = WScript.Arguments(0)

' Create a Shell object
RunPythonScript venvPath, scriptPath, argPath

' Function to run the Python script
Sub RunPythonScript(arg)
    ' Create a Shell object
    Set shell = CreateObject("WScript.Shell")

    ' Construct the command to activate the virtual environment and run the script with an argument
    command = "cmd /c """ & venvPath & "\Scripts\activate && python """ & scriptPath & """ """ & arg & """"
    ' Run the command
    shell.Run command, 1, True

    ' Clean up
    Set shell = Nothing
End Sub