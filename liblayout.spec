Name: liblayout
Version: 0.2.10
Release: %mkrel 5
Summary: CSS based layouting framework
License: LGPLv2+
Group:  System/Libraries 
Source: http://downloads.sourceforge.net/jfreereport/liblayout-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant, java-devel >= 0:1.6.0 , jpackage-utils, flute, libloader, xml-commons-apis, java-rpmbuild
BuildRequires: librepository, pentaho-libxml, libfonts, sac, libbase >= 1.1.3
Requires: java >= 0:1.6.0 , jpackage-utils, flute, libloader >= 1.1.3
Requires: librepository >= 1.1.3, libfonts >= 1.1.3, sac, xml-commons-apis
Requires: pentaho-libxml, libbase >= 1.0.0
BuildArch: noarch

%description
LibLayout is a layouting framework. It is based on the Cascading StyleSheets
standard. The layouting expects to receive its content as a DOM structure
(although it does not rely on the W3C-DOM API).


%package javadoc
Summary: Javadoc for %{name}
Group:    Documentation 
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
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sat Jan 12 2013 umeabot <umeabot> 0.2.10-5.mga3
+ Revision: 357643
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Oct 14 2012 ennael <ennael> 0.2.10-4.mga3
+ Revision: 305445
- Documentation group

* Sat Jan 21 2012 kamil <kamil> 0.2.10-3.mga2
+ Revision: 198986
- rebuild against new libloader-1.1.6, new pentaho-libxml-1.1.6, new libfonts-1.1.6 and new libbase-1.1.6
- clean .spec

* Fri Mar 18 2011 dmorgan <dmorgan> 0.2.10-2.mga1
+ Revision: 74327
- Really build without gcj

* Wed Jan 26 2011 dmorgan <dmorgan> 0.2.10-1.mga1
+ Revision: 40220
- Adapt for mageia
- imported package liblayout

