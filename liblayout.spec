Summary:	CSS based layouting framework
Name:		liblayout
Version:	0.2.10
Release:	1
License:	LGPLv2+
Group:		System/Libraries 
Url:		http://reporting.pentaho.org/
Source0:	http://downloads.sourceforge.net/jfreereport/liblayout-%{version}.zip
BuildArch:	noarch
BuildRequires:	ant
BuildRequires:	flute
BuildRequires:	java-devel >= 0:1.6.0 
BuildRequires:	java-rpmbuild
BuildRequires:	jpackage-utils
BuildRequires:	libbase >= 1.1.3
BuildRequires:	libfonts
BuildRequires:	libloader
BuildRequires:	librepository
BuildRequires:	pentaho-libxml
BuildRequires:	sac
BuildRequires:	xml-commons-apis
Requires:	flute
Requires:	java >= 0:1.6.0 
Requires:	jpackage-utils
Requires:	libbase >= 1.0.0
Requires:	libloader >= 1.1.3
Requires:	librepository >= 1.1.3
Requires:	libfonts >= 1.1.3
Requires:	pentaho-libxml
Requires:	sac
Requires:	xml-commons-apis

%description
LibLayout is a layouting framework. It is based on the Cascading StyleSheets
standard. The layouting expects to receive its content as a DOM structure
(although it does not rely on the W3C-DOM API).

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java 
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

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
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

