# Arch setup

## Set keyboard layout

- ls /usr/share/kbd/keymaps/**/*.map.gz
- loadkeys en ru

## Connect to internet

- ip link
- iwctl
- device list
- station device scan
- station device get-networks
- station device connect SSID
- ping archlinux.org

## Update system clock

- timedatectl set-ntp true
- timedatectl status

## Partitioning

- cfdisk
    - EFI
    - Swap
    - Linux system

## Format the partitions

- mkfs.fat -F32 /dev/efi_part
- mkswap /dev/swap_part
- mkfs.btrfs /dev/root_part

## Mount file systems

- mount /dev/root_part /mnt
- swapon /dev/swap_part

## Install essential packages

- pacstrap /mnt base linux linux-firmware

## Configure the system

- genfstab -U /mnt >> /mnt/etc/fstab
- arch-chroot /mnt
- ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
- hwclock --systohc
- sudo pacman -S vim
- vim /etc/locale.gen
- locale-gen
- vim /etc/hostname
    - hostname
- vim /etc/hosts
    - 127.0.0.1   localhost
    - ::1         localhost
    - 127.0.1.1   hostname.localdomain    hostname
- passwd
- useradd -m name
- passwd name
- usermod -aG wheel,audio,video,optical,storage name
- pacman -S sudo
- EDITOR=vim visudo
- pacman -S grub efibootmgr dosfstools os-prober mtools
- mkdir /boot/EFI
- mount /dev/efi_part /boot/EFI
- grub-install --target=x86_64-efi --bootloader-id=GRUB --recheck
- vim /etc/default/grub
    - GRUB_DISABLE_OS_PROBER=false
- grub-mkconfig -o /boot/grub/grub.cfg
- pacman -S NetworkManager git alacritty
- systemctl enable NetworkManager
- exit
- umount -R /mnt
- reboot

## Graphics

- sudo pacman -S xf86-video-intel nvidia xorg xorg-xinit xwallpaper
- sudo pacman -S qtile base-devel dmenu
- git clone https://aur.archlinux.org/paru.git
- cd paru
- makepkg -si
- paru -S brave-bin ttf-jetbrains-mono exa neovim
- cp /etc/X11/xinit/xinitrc /home/name/.xinit
    - xbindkeys &
    - exec qtile start
- startx

## Installing main software

- sudo pacman -S xbindkeys p7zip alsa-tools pulseaudio bat
- sudo pacman -S pulseaudio-alsa pavucontrol light flameshot
- sudo pacman -S ranger htop neofetch gparted mtpfs jmptfs
- sudo pacman -S sxiv mpv zathura zathura-djvu zathura-pdf-mupdf thunar
- copy .bashrc ~/
- copy .xbindkeysrc ~/
- copy alacritty.yml .config/alacritty/
- copy config.py .config/qtile/
- copy init.vim .config/nvim/
- paru -S telegram-desktop rnote notion-app visual-studio-code-bin

## List of software

- base, linux, linux-firmware
- vim
- grub, efibootmgr, dosfstools, os-prober, mtools
- NetworkManager, git, alacritty
- xf86-video-intel, nvidia, xorg, xorg-init
- xwallpapers, qtile, base-devel, dmenu
- yay-git
- brave-bin ttf-jetbrains-mono exa neovim
- xbindkeys, p7zip, alsa-tools, pulseaudio
- pulseaudio-alsa, pavucontrol, light, flameshot
- ranger, htop, neofetch, gparted, mtpfs, jmptfs
- sxiv, zathura, zathura-djvu, zathura-pdf-mupdf, thunar
- telegram-desktop, rnote, notion-app, visual-studio-code-bin
- bat, xp-pen-tablet