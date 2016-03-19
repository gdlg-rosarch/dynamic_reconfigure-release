Name:           ros-kinetic-dynamic-reconfigure
Version:        1.5.43
Release:        0%{?dist}
Summary:        ROS dynamic_reconfigure package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/dynamic_reconfigure
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rosservice
Requires:       ros-kinetic-std-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin >= 0.5.87
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roscpp-serialization
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-std-msgs

%description
This unary stack contains the dynamic_reconfigure package which provides a means
to change node parameters at any time without having to restart the node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Mar 19 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.43-0
- Autogenerated by Bloom

* Tue Mar 15 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.42-0
- Autogenerated by Bloom

* Mon Mar 14 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.41-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.40-0
- Autogenerated by Bloom

