%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Ruby
Summary:	Inline::Ruby perl module
Summary(pl):	Modu³ perla Inline::Ruby
Name:		perl-Inline-Ruby
Version:	0.01
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	ruby >= 1.6.3
Requires:	ruby >= 1.6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Ruby - Write Perl subroutines and classes in Ruby.

%description -l pl
Modu³ Inline::Ruby - pozwalaj±cy na pisanie procedur i klas Perla w
Rubym.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
%{__make}

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
%{perl_sitearch}/Inline/Ruby.pm
%dir %{perl_sitearch}/auto/Inline/Ruby
%{perl_sitearch}/auto/Inline/Ruby/Ruby.bs
%attr(755,root,root) %{perl_sitearch}/auto/Inline/Ruby/Ruby.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
