Name: liblayout
Version: 0.2.10
Release: 10
Summary: CSS based layouting framework
License: LGPLv2+ and UCD

Source0: http://downloads.sourceforge.net/jfreereport/liblayout-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant, java-devel, jpackage-utils, flute, libloader
BuildRequires: librepository, pentaho-libxml, libfonts, sac, libbase >= 1.1.3
# We must build this with JDK <= 12.0 because it's used by
# libreoffice (which can't build with JDK > 12.0 due to
# hsqldb 1.8.x)
BuildRequires: java-12-openjdk-devel
Requires: java, jpackage-utils, flute, libloader >= 1.1.3
Requires: librepository >= 1.1.3, libfonts >= 1.1.3, sac
Requires: pentaho-libxml, libbase >= 1.0.0
BuildArch: noarch

%description
LibLayout is a layouting framework. It is based on the Cascading StyleSheets
standard. The layouting expects to receive its content as a DOM structure
(although it does not rely on the W3C-DOM API).

%package javadoc
Summary: Javadoc for %{name}

Requires: %{name} = %{version}-%{release}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
export JAVA_HOME=%{_prefix}/lib/jvm/java-12-openjdk
export PATH=$JAVA_HOME/bin:$PATH

find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib flute libloader librepository libxml libfonts \
    sac libbase commons-logging-api

%build
export JAVA_HOME=%{_prefix}/lib/jvm/java-12-openjdk
export PATH=$JAVA_HOME/bin:$PATH
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/java
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_datadir}/java/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_datadir}/java/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_datadir}/javadoc/%{name}
