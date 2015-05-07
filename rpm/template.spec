Name:           ros-indigo-world-item-observer
Version:        0.0.1
Release:        0%{?dist}
Summary:        ROS world_item_observer package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/world_item_search
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-graspdb
Requires:       ros-indigo-rail-manipulation-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-worldlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-graspdb
BuildRequires:  ros-indigo-rail-manipulation-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-ros
BuildRequires:  ros-indigo-worldlib

%description
Persistent Observer of Items in the World for the Spatial World Database

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu May 07 2015 Russell Toris <rctoris@wpi.edu> - 0.0.1-0
- Autogenerated by Bloom

