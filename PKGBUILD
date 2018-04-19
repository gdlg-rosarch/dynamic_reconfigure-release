# Script generated with Bloom
pkgdesc="ROS - This unary stack contains the dynamic_reconfigure package which provides a means to change node parameters at any time without having to restart the node."
url='http://ros.org/wiki/dynamic_reconfigure'

pkgname='ros-lunar-dynamic-reconfigure'
pkgver='1.5.49_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-lunar-catkin>=0.5.87'
'ros-lunar-message-generation'
'ros-lunar-roscpp'
'ros-lunar-roscpp-serialization'
'ros-lunar-rostest'
'ros-lunar-std-msgs'
)

depends=('boost'
'ros-lunar-message-runtime'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-rospy'
'ros-lunar-rosservice'
'ros-lunar-std-msgs'
)

conflicts=()
replaces=()

_dir=dynamic_reconfigure
source=()
md5sums=()

prepare() {
    cp -R $startdir/dynamic_reconfigure $srcdir/dynamic_reconfigure
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

