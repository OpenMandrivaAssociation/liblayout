%{?_javapackages_macros:%_javapackages_macros}
Name: liblayout
Version: 0.2.10
Release: 8.0%{?dist}
Summary: CSS based layouting framework
License: LGPLv2+ and UCD

Source: http://downloads.sourceforge.net/jfreereport/liblayout-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant, java-devel, jpackage-utils, flute, libloader, xml-commons-apis
BuildRequires: librepository, pentaho-libxml, libfonts, sac, libbase >= 1.1.3
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: java, jpackage-utils, flute, libloader >= 1.1.3
Requires: librepository >= 1.1.3, libfonts >= 1.1.3, sac, xml-commons-apis
Requires: pentaho-libxml, libbase >= 1.0.0
BuildArch: noarch

%description
LibLayout is a layouting framework. It is based on the Cascading StyleSheets
standard. The layouting expects to receive its content as a DOM structure
(although it does not rely on the W3C-DOM API).

%package javadoc
Summary: Javadoc for %{name}

Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib flute libloader librepository libxml libfonts \
    sac jaxp libbase commons-logging-api

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 03 2012 Caolán McNamara <caolanm@redhat.com> - 0.2.10-6
- resource/GraphemeBreakProperty.txt and liblayout-0.2.10.zip/resource/Blocks.txt are
  under UCD

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> - 0.2.10-3
- Related: rhbz#749103 drop gcj aot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 03 2009 Caolan McNamara <caolanm@redhat.com> 0.2.10-1
- latest version

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 0.2.9-4.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Mon Mar 16 2009 Caolan McNamara <caolanm@redhat.com> 0.2.9-3.OOo31
- Post-release tuned for OpenOffice.org

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Caolan McNamara <caolanm@redhat.com> 0.2.9-1
- initial fedora import
