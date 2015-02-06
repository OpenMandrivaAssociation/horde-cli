%define prj    Horde_CLI

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-cli
Version:       0.0.2
Release:       3
Summary:       Horde CLI API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-gettext
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
Horde_CLI:: API for basic command-line functionality/checks

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%{peardir}/Horde/CLI.php


%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2011.0
+ Revision: 560535
- Increased release for rebuild

* Sun Feb 21 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 509324
- replace PreRqu with Requires(pre)
- import horde-cli


