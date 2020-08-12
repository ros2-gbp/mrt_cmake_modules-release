%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-mrt-cmake-modules
Version:        1.0.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mrt_cmake_modules package

License:        BSD
URL:            http://wiki.ros.org/mrt_cmake_modules
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       lcov
Requires:       python3-PyYAML
Requires:       python3-catkin_pkg
Requires:       python3-rospkg
Requires:       python3-setuptools
Requires:       ros-noetic-ros-environment
BuildRequires:  python3-PyYAML
BuildRequires:  python3-catkin_pkg
BuildRequires:  python3-rospkg
BuildRequires:  python3-setuptools
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-ros-environment
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
CMake Functions and Modules for automating CMake

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Aug 12 2020 Fabian Poggenhans <fabian.poggenhans@kit.edu> - 1.0.4-1
- Autogenerated by Bloom

* Wed Jun 03 2020 Fabian Poggenhans <fabian.poggenhans@kit.edu> - 1.0.3-1
- Autogenerated by Bloom

