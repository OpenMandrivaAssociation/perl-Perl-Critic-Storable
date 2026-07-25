%define upstream_name    Perl-Critic-Storable
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Perl::Critic policy for using Storable
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Perl-Critic-Storable
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MATTD/Perl-Critic-Storable-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
An additional Perl::Critic policy for using the Storable module:

* * the Perl::Critic::Policy::Storable::ProhibitStoreOrFreeze manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 653613
- rebuild for updated spec-helper

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 575424
- import perl-Perl-Critic-Storable

