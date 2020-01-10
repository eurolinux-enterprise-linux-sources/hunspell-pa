Name: hunspell-pa
Summary: Punjabi hunspell dictionaries
Version: 20050726
Release: 10%{?dist}
Source: http://hunspell.sourceforge.net/pa-demo.tar.gz
Group: Applications/Text
URL: http://hunspell.sourceforge.net
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Punjabi hunspell dictionaries.

%prep
%setup -q -c -n pa-demo
iconv -f ISO-8859-1 -t UTF-8 pa/Copyright > pa/Copyright.utf8
mv pa/Copyright.utf8 pa/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mv pa/pa.dic pa/pa_IN.dic
mv pa/pa.aff pa/pa_IN.aff
cp -p pa/*.dic pa/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc pa/README pa/COPYING pa/Copyright
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20050726-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade AT redhat DOT com> - 20050726-7
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20050726-2
- Added Copyright

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20050726-1
- Initial Fedora release
