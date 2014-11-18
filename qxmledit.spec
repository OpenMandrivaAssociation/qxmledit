Name:           qxmledit
Version:        0.8.11
Release:        1
Summary:        Simple XML editor and XSD viewer
Group:          Editors
License:        GPLv2
URL:            http://code.google.com/p/qxmledit
Source:         http://qxmledit.googlecode.com/files/%{name}-%{version}-src.tgz

BuildRequires:  qt4-devel


%description
QXmlEdit is a simple XML editor written in qt4. Its main features are unusual
data visualization modes, nice XML manipulation and presentation.
It can split very big XML files into fragments, and compare XML files.
It is one of the few graphical Open Source XSD viewers. 

%prep
%setup -q


%build
%global optflags %{optflags} -Wno-strict-aliasing
%qmake_qt4 QXmlEdit.pro
%make \
	QXMLEDIT_INST_DATA_DIR=%{_datadir}/%{name} \
	QXMLEDIT_INST_DIR=%{_bindir} \
	QXMLEDIT_INST_DOC_DIR=%{_datadir}/doc/%{name} \
	QXMLEDIT_INST_LIB_DIR=%{_libdir} \
	QXMLEDIT_INST_INCLUDE_DIR=%{_includedir}/%{name}

%install
%make INSTALL_ROOT=%{buildroot} install
rm -fr %{buildroot}%{_includedir} %{buildroot}%{_libdir}/*.so

ln -sf %{_bindir}/QXmlEdit %{buildroot}%{_bindir}/%{name}

%__install -Dm 0644 ./src/images/icon.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -Dm 0644 ./src/images/icon.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#fix wrong-script-end-of-line-encoding 
perl -pi -e 's/\r/\n/g' ./src/findtextparams.h
perl -pi -e 's/\r/\n/g' ./src/globals/includes/xmleditwidget.h
perl -pi -e 's/\r/\n/g' ./src/xmleditwidget.cpp


%__mkdir_p %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=QXmlEdit
GenericName=Simple XML Editor and XSD viewer
Comment=Simple XML Editor and XSD viewer
Type=Application
Exec=QXmlEdit %u
Icon=qxmledit
Categories=Qt;Utility;TextEditor;
MimeType=text/xml;application/xml;
StartupNotify=true
Terminal=false
EOF


%files
%doc AUTHORS COPYING DISTRIBUTING GPLV3.txt LGPLV3.txt INSTALL NEWS README ROADMAP TODO doc/QXmlEdit_manual.pdf
%{_bindir}/QXmlEdit
%{_bindir}/%{name}
%{_libdir}/libQXmlEdit*.so.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}.*
