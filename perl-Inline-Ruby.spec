#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Ruby
Summary:	Inline::Ruby - write Perl subroutines and classes in Ruby
Summary(pl):	Inline::Ruby - pisanie funkcji i klas Perla w jêzyku Ruby
Name:		perl-Inline-Ruby
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	decffede80bc61e9772068a6424eb3ac
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

%description -l pl
Inline::Ruby pozwala na pisanie funkcji i klas Perla w jêzyku Ruby.
Dynamicznie t³umaczy parametry i zwracane warto¶ci na typy danych
natywne dla obu jêzyków oraz wie, jak przekszta³ciæ wiêkszo¶æ innych
typów danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/auto/Inline/Ruby/Ruby.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Inline/Ruby/Ruby.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
