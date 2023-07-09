Name:           vpcs
Version:        0.8.2
Release:        1%{?dist}
Summary:        Virtual PC Simulator

License:        BSD
URL:            https://github.com/GNS3/vpcs/
Source0:        https://github.com/GNS3/vpcs/archive/v0.8.2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  make
BuildRequires:  gcc

%description
The VPCS can simulate up to 9 PCs. You can ping/traceroute them, or 
ping/traceroute the other hosts/routers from the VPCS

%global debug_package %{nil}

%prep
%autosetup -p1

%build
cd src/
./mk.sh

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man1/
install -m 755 src/%{name} %{buildroot}/%{_bindir}
install -m 644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/ 

%files
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%doc readme.txt

%changelog
* Wed Nov 17 2021 Tsvetan Gerov <tsvetan@georv.eu> - 0.8.2-1
- Bump version to 0.8.2, based on GNS3 VPCS Repoistory

* Thu Mar 18 2021 Tsvetan Gerov <tsvetan@gerov.eu> - 0.8.1-1
- Bump version to 0.8.1, based on GNS3 VPCS Repository

* Thu Dec 01 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.8-3
- Fix Source url and nvr

* Tue Sep 27 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.8.0.20160224svn-2
- Fix version

* Sat Sep 10 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.8.0svn126-1
- Update to latest svn rev to fix some bugs

* Sat Sep 10 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.8-1
- Initial spec
