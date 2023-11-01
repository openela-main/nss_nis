Name:           nss_nis
Version:        3.0
Release:        8%{?dist}
Summary:        Name Service Switch (NSS) module using NIS
License:        LGPLv2+
Group:          System Environment/Base
Url:            https://github.com/thkukuk/libnss_nis
Source:         https://github.com/thkukuk/libnss_nis/archive/v%{version}.tar.gz

# https://github.com/systemd/systemd/issues/7074
Source2:        nss_nis.conf

BuildRequires:  libnsl2-devel
BuildRequires:  libtirpc-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires:  systemd


%description
The nss_nis Name Service Switch module uses the Network Information System (NIS)
to obtain user, group, host name, and other data.

%prep
%setup -q -n libnss_nis-%{version}

%build

export CFLAGS="%{optflags}"

autoreconf -fiv

%configure --libdir=%{_libdir} --includedir=%{_includedir}
%make_build

%install
%make_install
rm  %{buildroot}/%{_libdir}/libnss_nis.{a,la}
rm  %{buildroot}/%{_libdir}/libnss_nis.so

install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/systemd-logind.service.d/nss_nis.conf

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_libdir}/libnss_nis.so.2
%{_libdir}/libnss_nis.so.2.0.0
%{_unitdir}/systemd-logind.service.d/*


%license COPYING

%changelog
* Mon Jan 28 2019 Matej Mužila <mmuzila@redhat.com> 3.0-8
- Add systemd-logind snippet (RestrictAddressFamilies)
  Resolves: #1647911

* Wed Aug 1 2018 Matej Mužila <mmuzila@redhat.com> - 3.0-7
- BuildRequire systemd

* Wed Aug 1 2018 Matej Mužila <mmuzila@redhat.com> - 3.0-6
- Add systemd-logind snippet (IPAddressAllow=any)
- Resolves: #1574959

* Tue Jan 30 2018 Matej Mužila <mmuzila@redthat.com> - 3.0-3
- Inital release
