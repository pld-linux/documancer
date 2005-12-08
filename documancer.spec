Summary:	Programmer's documentation reader
Name:		documancer
Version:	0.2.6
Release:	0.1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/documancer/%{name}-%{version}.tar.gz
# Source0-md5:	f570655370c232a2947699258fc6fae0
URL:		http://documancer.sourceforge.net/
Requires:	python-wxPython
requires:	wxMozilla
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Documancer is programmer's documentation reader with very fast fulltext searching.

%prep
%setup -q

%build
%configure \
	--libdir=%{_datadir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/documancer/providers/man/man2html/man2html \
	$RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/man2html $RPM_BUILD_ROOT%{_datadir}/documancer/providers/man/man2html/man2html

rm -f $RPM_BUILD_ROOT%{_bindir}/documancer
echo '#!/usr/bin/python %{_datadir}/documancer/documancer.py' > $RPM_BUILD_ROOT%{_bindir}/documancer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/documancer
%attr(755,root,root) %{_bindir}/man2html
%{_datadir}/documancer
# /usr/share/documancer/indexers/java/documancer-java-indexer needs to be 755
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
