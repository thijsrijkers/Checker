command -v git >/dev/null 2>&1 ||
{ echo >&2 "Git is not installed.";
    $SHELL
}
mkdir -p C:/Bamboo
mkdir -p C:/Bamboo/Resources
xcopy "Resources\Window.sh" "C:\Bamboo\Resources"
ls -lt
ln -s C:/Bamboo/Resources/Window.sh $HOME/Desktop
