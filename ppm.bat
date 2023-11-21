@echo off
setlocal enabledelayedexpansion

REM List of unavailable packages
set "unavailablePackages=ursina Ursina Pyinstaller pyautogui PyAutoGui Pyautogui PyAutogui PyautoGui"

REM Check if no arguments are passed
if "%1"=="" (
    goto NOARGS
)

set "action=%1"
set "package=%2"

if /i "%action%"=="install" (
    if not "%package%"=="" (
        call :CheckPackageAvailability
    ) else (
        goto NOPACKAGEARG
    )
) else if /i "%action%"=="uninstall" (
    if not "%package%"=="" (
        call :CheckPackageAvailability
    ) else (
        goto NOPACKAGEARG
    )
) else (
    echo Invalid argument. Please use "install" or "uninstall".
    goto :EOF
)

:CheckPackageAvailability
set "packageAvailable=true"

for %%i in (%unavailablePackages%) do (
    if /i "!package!"=="%%i" (
        echo Package unavailable: !package!
        set "packageAvailable=false"
        goto :EOF
    )
)

if %packageAvailable%==true (
    if /i "%action%"=="install" (
        echo Installing package %package%...
        python.exe -m pip install --upgrade pip -q>NUL
        python -m pip install "!package!" -q>NUL
    ) else if /i "%action%"=="uninstall" (
        echo Uninstalling package %package%...
        python.exe -m pip install --upgrade pip -q>NUL
        python -m pip uninstall "!package!" -q>NUL
    )
)
goto :EOF

:NOARGS
echo Hello, %USERNAME%
echo --------------------
echo PPM Version 1.1 BETA
echo Build code 111923
goto :EOF

:NOPACKAGEARG
echo Wrong usage! Example:
echo ppm install [package]
goto :EOF
