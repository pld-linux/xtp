Summary:	xtp - file transfer program
Summary(pl):	xtp - program do przesy³ania plików
Name:		xtp
Version:	5.4.3
Release:	1
License:	BSD-like
Group:		Applications/Networking
Source0:	ftp://ftp.simplesystems.org/pub/ImageMagick/delegates/%{name}-%{version}.tar.gz
# Source0-md5:	0748b0f991fb92503132e1412fedd0ad
Patch0:		%{name}-nolibs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtp is a utility for retrieving, listing, or printing files from a
remote network site, or sending files to a remote network site. xtp
performs most of the same functions as the ftp(1) program, but does
not require any interactive commands. You simply specify the file
transfer task on the command line and xtp performs the task
automatically.

%description -l pl
xtp to narzêdzie do pobierania, listowania lub wypisywania plików ze
zdalnych komputerów w sieci oraz do wysy³ania plików na zdalne
komputery. xtp wykonuje wiêkszo¶æ funkcji programu ftp(1), ale nie
wymaga ¿adnych interaktywnych poleceñ. Po prostu z linii poleceñ
podaje siê zadanie przes³ania pliku, a xtp wykonuje je automatycznie.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
