#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Script
Summary:	Test::Script - Cross-platform basic tests for scripts
Name:		perl-Test-Script
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	affeb47b8c7b9f1eb6ff346daa85784d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPC-Run3
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
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
