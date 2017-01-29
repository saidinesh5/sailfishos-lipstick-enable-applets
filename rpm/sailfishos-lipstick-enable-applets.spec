# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-lipstick-enable-applets

# >> macros
BuildArch: noarch
# << macros

Summary:    Enable applet layer in lipstick
Version:    0.0.2
Release:    1
Group:      Qt/Qt
License:    BSD
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   lipstick-jolla-home-qt5 >= 0.22.44.7

%description
A lipstick patch to enable applets.
Applets are tiny hovering overlay windows for a nicer multitasking experrience


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-lipstick-enable-applets
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-lipstick-enable-applets
# << install pre

# >> install post
# << install post

%pre
# >> pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-lipstick-enable-applets || true
fi
# << pre

%preun
# >> preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-lipstick-enable-applets || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-lipstick-enable-applets
# >> files
# << files
