#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Script
Summary:	Test::Script - Cross-platform basic tests for scripts
Summary(pl.UTF-8):	Test::Script - wieloplatformowe podstawowe testy dla skryptów
Name:		perl-Test-Script
Version:	1.29
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cadfb1d1fdc421e338521e373d7a9eb7
URL:		https://metacpan.org/release/Test-Script
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Capture-Tiny
BuildRequires:	perl-Probe-Perl >= 0.01
BuildRequires:	perl-Test-Simple >= 1.302015
BuildRequires:	perl-Test2-Suite >= 0.000060
BuildRequires:	perl-Text-ParseWords
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The intent of this module is to provide a series of basic tests for
scripts in the bin directory of your Perl distribution. Further, it
aims to provide them with perfect platform-compatibility and in a way
that is as unobtrusive as possible. That is, if the program works on a
platform, then Test::Script should also work on that platform. In
doing so, it is hoped that Test::Script can become a module that you
can safely make a dependency of your module, without risking your
module not working on some platform because of the dependency. Where a
clash exists between wanting more functionality and maintaining
platform safety, this module will err on the side of platform safety.

%description -l pl.UTF-8
Przeznaczeniem tego modułu jest zapewnienie serii podstawowych testów
dla skryptów z katalogu bin pakietu perlowego. Ponadto ma na celu
udostępnienie im doskonałej kompatybilności z platformami w możliwie
niekłopotliwy sposób. Oznacza to, że jeśli program działa na jakiejś
platformie, Test::Script także powinien na tej platformie działać.
Przy tym Test::Script powinien stać się modułem, który bezpiecznie
można uczynić zależnością własnego modułu bez ryzykowania, że moduł
przestanie działać na jakiejś platformie z powodu tej zależności. Tam,
gdzie występuje kolizja między większą funkcjonalnością a zachowaniem
zgodności z platformą, ten moduł stanie po stronie zgodności.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/Script.pm
%{_mandir}/man3/Test::Script.3pm*
