#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Ruby
Summary:	Inline::Ruby Perl module
Summary(cs):	Modul Inline::Ruby pro Perl
Summary(da):	Perlmodul Inline::Ruby
Summary(de):	Inline::Ruby Perl Modul
Summary(es):	M�dulo de Perl Inline::Ruby
Summary(fr):	Module Perl Inline::Ruby
Summary(it):	Modulo di Perl Inline::Ruby
Summary(ja):	Inline::Ruby Perl �⥸�塼��
Summary(ko):	Inline::Ruby �� ����
Summary(no):	Perlmodul Inline::Ruby
Summary(pl):	Modu� Perla Inline::Ruby
Summary(pt):	M�dulo de Perl Inline::Ruby
Summary(pt_BR):	M�dulo Perl Inline::Ruby
Summary(ru):	������ ��� Perl Inline::Ruby
Summary(sv):	Inline::Ruby Perlmodul
Summary(uk):	������ ��� Perl Inline::Ruby
Summary(zh_CN):	Inline::Ruby Perl ģ��
Name:		perl-Inline-Ruby
Version:	0.02
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	decffede80bc61e9772068a6424eb3ac
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	ruby >= 1.6.3
Requires:	ruby >= 1.6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Ruby - Write Perl subroutines and classes in Ruby.

%description -l pl
Modu� Inline::Ruby - pozwalaj�cy na pisanie procedur i klas Perla w
Rubym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"
%{!?_without_tests:%{__make} test}

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
