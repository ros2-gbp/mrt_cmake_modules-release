%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-mrt-cmake-modules
Version:        1.0.11
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mrt_cmake_modules package

License:        BSD
URL:            http://wiki.ros.org/mrt_cmake_modules
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       lcov
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-rospkg
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-yaml
Requires:       ros-iron-gtest-vendor
Requires:       ros-iron-ros-environment
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  python%{python3_pkgversion}-rospkg
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  ros-iron-ament-cmake-core
BuildRequires:  ros-iron-ros-environment
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
CMake Functions and Modules for automating CMake

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
    -DCATKIN_ENABLE_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%files
/opt/ros/iron

%changelog
* Mon Sep 23 2024 Kevin Rösch <kevin.roesch@kit.edu> - 1.0.11-1
- Autogenerated by Bloom

* Mon Aug 19 2024 Kevin Rösch <kevin.roesch@kit.edu> - 1.0.10-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Kevin Rösch <kevin.roesch@kit.edu> - 1.0.9-4
- Autogenerated by Bloom

* Tue Mar 21 2023 Kevin Rösch <kevin.roesch@kit.edu> - 1.0.9-3
- Autogenerated by Bloom

