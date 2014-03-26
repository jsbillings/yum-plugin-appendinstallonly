Name:           yum-plugin-appendinstallonly
Version:        0.6
Release:        1%{?dist}
Summary:        Yum Plugin to allow you to append to installonlypkgs

License:        GPL
URL:            https://github.com/jsbillings/yum-plugin-appendinstallonly
Source0:        yum-plugin-appendinstallonly-%{version}.tar.gz

Requires:       yum

%description
A plugin for yum which will add to the installonlypkgs directive
without overwritting what's in /etc/yum.conf or overriding the
defaults contained in yum's config.py code 

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -D -p -m 0755 appendinstallonly.py $RPM_BUILD_ROOT/%{_prefix}/lib/yum-plugins/appendinstallonly.py
install -D -p -m 0644 appendinstallonly.conf $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/appendinstallonly.conf

%files
%doc README.md COPYING
%{_prefix}/lib/yum-plugins/appendinstallonly.py*
%{_sysconfdir}/yum/pluginconf.d/appendinstallonly.conf

%changelog
* Wed Mar 26 2014 Jonathan Billings <jsbillin@umich.edu> 0.6-1
- Spec File: include compiled python (jsbillin@umich.edu)

* Wed Mar 26 2014 Jonathan Billings <jsbillin@umich.edu> 0.5-1
- Spec File: fixed install again (jsbillin@umich.edu)

* Wed Mar 26 2014 Jonathan Billings <jsbillin@umich.edu> 0.4-1
- Spec file: fix source in install (jsbillin@umich.edu)

* Wed Mar 26 2014 Jonathan Billings <jsbillin@umich.edu> 0.3-1
- Spec file: fix sources (jsbillin@umich.edu)

* Wed Mar 26 2014 Jonathan Billings <jsbillin@umich.edu> 0.2-1
- new package built with tito

* Wed Mar 26 2014 Jonathan S. Billings <jsbillin@umich.edu>
- Initial package creation
