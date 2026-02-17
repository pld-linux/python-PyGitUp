#
# Conditional build:
%bcond_with	tests	# unit tests (need git configured for user)

%define		module	PyGitUp
Summary:	git-up(1) - fetch and rebase all locally-tracked remote branches
Summary(pl.UTF-8):	git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych gałęzi
Name:		python-%{module}
Version:	2.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/msiemens/PyGitUp/releases
Source0:	https://github.com/msiemens/PyGitUp/archive/v%{version}/%{module}-v%{version}.tar.gz
# Source0-md5:	c722574b2a9554517dd2614a8a43362d
URL:		https://github.com/msiemens/PyGitUp
%{?with_tests:BuildRequires:	git-core}
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-build
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-click >= 7.0
BuildRequires:	python3-colorama >= 0.3.7
BuildRequires:	python3-git >= 2.1.8
BuildRequires:	python3-nose >= 1.3.7
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-termcolor >= 1.1.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-up(1) - fetch and rebase all locally-tracked remote branches.

%description -l pl.UTF-8
git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych
gałęzi.

%package -n python3-%{module}
Summary:	git-up(1) - fetch and rebase all locally-tracked remote branches
Summary(pl.UTF-8):	git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych gałęzi
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.10

%description -n python3-%{module}
git-up(1) - fetch and rebase all locally-tracked remote branches.

%description -n python3-%{module} -l pl.UTF-8
git-up(1) - pobieranie i rebase wszystkich śledzonych lokalnie zdanych
gałęzi.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/PyGitUp/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENCE README.rst
%attr(755,root,root) %{_bindir}/git-up
%dir %{py3_sitescriptdir}/PyGitUp
%{py3_sitescriptdir}/PyGitUp/*.py
%{py3_sitescriptdir}/PyGitUp/__pycache__
%{py3_sitescriptdir}/git_up-%{version}.dist-info
