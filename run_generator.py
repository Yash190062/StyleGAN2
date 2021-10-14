CRP1 = '"%PROGRAMFILES(X86)%\Google\Chrome Remote Desktop\CurrentVersion\remoting_start_host.exe" --code="4/0AX4XfWisfk8tHQuwCXdJ7oZ5g3D1vfGBfY6SfubKeqcMCUhK4rGBylExMCuOXc_b3JFysQ" --redirect-url="https://remotedesktop.google.com/_/oauthredirect" --name=%COMPUTERNAME%'
Pin = 123456 ## rdp pin
Name = "RDP"    ## rdp name
import os,subprocess
username = "user" 
password = "root"
print("Creating User and Setting it up")
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")
print("User Created and Configured")
CRP = CRP1.replace("$(hostname)",Name)
class CRD:
    def __init__(self):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChorme()
        self.installingEdge()
        self.installingBrave()
        self.installwine()
        self.installingOBS()
        self.finish()
    @staticmethod
    def installCRD():
        print("Installing Chrome Remote Desktop")
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")

    @staticmethod
    def installGoogleChorme():
        print("Installing Google Chrome")
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
    
    @staticmethod
    def installingEdge():
        print("Installing edge Browser")
        subprocess.run(["wget", "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-dev/microsoft-edge-dev_93.0.926.1-1_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "microsoft-edge-dev_93.0.926.1-1_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
    
    @staticmethod
    def installingBrave():
        print("Installing Brave Browser")
        subprocess.run(["wget", "https://github.com/brave/brave-browser/releases/download/v1.28.31/brave-browser-nightly_1.28.31_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "brave-browser-nightly_1.28.31_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
    
    @staticmethod
    def installwine():
        print ("installing wine")
        ! sudo dpkg --add-architecture i386
        ! sudo apt update
        ! apt-get install -y wine32
        ! sudo apt -y install gnupg2 software-properties-common
        ! wget -qO - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add 
        ! sudo apt-add-repository https://dl.winehq.org/wine-builds/debian/
        ! sudo apt update
        ! wget -O- -q https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/Debian_9.0/Release.key | sudo apt-key add -    
        ! echo "deb http://download.opensuse.org/repositories/Emulators:/Wine:/Debian/Debian_9.0 ./" | sudo tee /etc/apt/sources.list.d/wine-obs.list
        ! sudo apt-get update
        ! sudo apt install --install-recommends winehq-stable
        ! wine --version

    @staticmethod
    def installingOBS():
        print("Installing OBS-STUDIO")
        package = "obs-studio"
        ! apt --fix-broken install > /dev/null 2>&1
        ! killall apt > /dev/null 2>&1
        ! rm /var/lib/dpkg/lock-frontend
        ! dpkg --configure -a > /dev/null 2>&1
        ! apt-get  install -o Dpkg::Options::="--force-confold" --no-install-recommends -y $package
        ! dpkg --configure -a > /dev/null 2>&1
        ! apt  update > /dev/null 2>&1
        ! apt install $package > /dev/null 2>&1

    @staticmethod
    def finish():
        print("Finalizing")
        os.system(f"adduser {username} chrome-remote-desktop")
        command = f"{CRP} --pin={Pin}"
        os.system(f"su - {username} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        print("Finished Succesfully")

try:
    if username:
        if CRP == "":
            print("Please enter authcode from the given link")
        elif len(str(Pin)) < 6:
            print("Enter a pin more or equal to 6 digits")
        else:
            CRD()
except NameError as e:
    print("username variable not found")
    print("Create a User First")
