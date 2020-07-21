rem Go to a temporary directory not to pollute file system

cd %1

set files=

(for /r %%a in (*.vhd) do (
	if NOT %%a == %2 call set files=%%files%% "%%a"
))

cd %temp%

rem Actually call the source code linter
xvhdl --nolog "%3" %files% 

rem Store error code to return after
set return_code=%errorlevel%

rem Delete generated files
call del /f xvhdl.pb
call rmdir /q /s xsim.dir

rem Exit with previously stored return code
exit /b %return_code%