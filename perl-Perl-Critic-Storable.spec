%define upstream_name    Perl-Critic-Storable
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl::Critic policy for using Storable
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
An additional Perl::Critic policy for using the Storable module:

* * the Perl::Critic::Policy::Storable::ProhibitStoreOrFreeze manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


