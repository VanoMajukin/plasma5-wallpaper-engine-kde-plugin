%define glslang_ver 11.8.0

Name: plasma5-wallpaper-engine-kde-plugin
Version:0.5.4
Release: alt1

Summary: A wallpaper plugin integrating wallpaper engine into kde wallpaper setting
License: GPL-2.0
Group: Graphical desktop/KDE
Url: https://github.com/catsout/wallpaper-engine-kde-plugin

# Source-url: https://github.com/catsout/wallpaper-engine-kde-plugin/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/KhronosGroup/glslang/archive/refs/tags/%glslang_ver.tar.gz
Source1: glslang.tar

Patch: plasma5-wallpaper-engine-kdeplugin-0.5.4-alt-fix-build-gcc13.patch
Patch2: plasma5-wallpaper-engine-kdeplugin-0.5.4-alt-fix-pyext.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: plasma5-workspace-devel plasma5-workspace-qml glslang-devel glslc
BuildRequires: kf5-plasma-framework-devel kf5-kpackage-devel kf5-kcoreaddons-devel kf5-kservice-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-libav
BuildRequires: liblz4-devel
BuildRequires: libmpv-devel
BuildRequires: python3-module-websockets
BuildRequires: qt5-base-devel qt5-webchannel-devel qt5-x11extras-devel qt5-websockets-devel

Requires: python3-module-websockets

%description
%summary

%prep
%setup -a1
%patch -p1
%patch2 -p1

%build
%cmake -DUSE_PLASMAPKG=OFF
%cmake_build

%install
%cmake_install
install -Dm 644 %buildroot%_libdir/qml/com/github/catsout/wallpaperEngineKde/libWallpaperEngineKde.so %buildroot%_libdir/qt5/qml/com/github/catsout/wallpaperEngineKde/libWallpaperEngineKde.so
install -Dm 644 %buildroot%_libdir/qml/com/github/catsout/wallpaperEngineKde/qmldir %buildroot%_libdir/qt5/qml/com/github/catsout/wallpaperEngineKde/qmldir
rm -rf %buildroot%_libdir/qml

%files
%_libdir/qt5/qml/com/github/catsout/wallpaperEngineKde/libWallpaperEngineKde.so
%_libdir/qt5/qml/com/github/catsout/wallpaperEngineKde/qmldir
%_datadir/kf5/plasma/wallpapers/com.github.casout.wallpaperEngineKde/
%_datadir/kservices5/plasma-wallpaper-com.github.casout.wallpaperEngineKde.desktop
%_datadir/metainfo/com.github.casout.wallpaperEngineKde.appdata.xml

%changelog
* Tue Aug 15 2023 Ivan Mazhukin <vanomj@altlinux.org> 0.5.4-alt1
- Initial build for Alt Sisyphus

