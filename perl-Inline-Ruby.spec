#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Ruby
Summary:	Inline::Ruby - write Perl subroutines and classes in Ruby
Summary(pl.UTF-8):	Inline::Ruby - pisanie funkcji i klas Perla w języku Ruby
Name:		perl-Inline-Ruby
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	decffede80bc61e9772068a6424eb3ac
URL:		http://search.cpan.org/dist/Inline-Ruby/
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.6.3
Requires:	ruby >= 1:1.6.3
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Ruby lets you write Perl subroutines and classes in Ruby. It
dynamically translates the parameters and return values into native data
types for both languages -- and it knows how to "wrap" most other types
of data.

%description -l pl.UTF-8
Inline::Ruby pozwala na pisanie funkcji i klas Perla w języku Ruby.
Dynamicznie tłumaczy parametry i zwracane wartości na typy danych
natywne dla obu języków oraz wie, jak przekształcić większość innych
typów danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Inline/Ruby.pm
%dir %{perl_vendorarch}/auto/Inline/Ruby
%attr(755,root,root) %{perl_vendorarch}/auto/Inline/Ruby/Ruby.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
