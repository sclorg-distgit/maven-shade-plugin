%{?scl:%scl_package maven-shade-plugin}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-shade-plugin
Version:        3.0.0
Release:        2.1%{?dist}
Summary:        This plugin provides the capability to package the artifact in an uber-jar
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{pkg_name}
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

Patch0:         0001-Port-to-maven-dependency-tree-3.0.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(com.google.guava:guava)
BuildRequires:  %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  %{?scl_prefix}mvn(org.jdom:jdom)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm)
BuildRequires:  %{?scl_prefix}mvn(org.ow2.asm:asm-commons)
BuildRequires:  %{?scl_prefix}mvn(org.vafer:jdependency)

%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade - i.e. rename - the
packages of some of the dependencies.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
%{summary}.

%prep
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1
rm src/test/jars/plexus-utils-1.4.1.jar
ln -s $(build-classpath plexus/utils) src/test/jars/plexus-utils-1.4.1.jar

%build
# A class from aopalliance is not found. Simply adding BR does not solve it
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.0.0-2.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Michael Simacek <msimacek@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Mon May 02 2016 Michael Simacek <msimacek@redhat.com> - 2.4.3-1
- Update to upstream version 2.4.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-1
- Update to upstream version 2.4.2

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-3
- Fix Maven 3 patch

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-2
- Port to maven-dependency-tree 3.0

* Thu Jul 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-1
- Update to upstream version 2.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-1
- Update to upstream version 2.4

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-5
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-4
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-2
- Add patch for MSHADE-168
- Resolves: rhbz#1096583

* Fri May  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Dec  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-1
- Update to upstream version 2.2

* Tue May 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-1
- Update to upstream version 2.1

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec 13 2012 Tomas Radej <tradej@redhat.com> - 2.0-1
- Update to upstream 2.0

* Wed Nov 14 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.1-3
- Install NOTICE file with javadoc package

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.7.1-1
- Update to upstream 1.7.1.

* Wed Jun 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-1
- Update to upstream 1.7

* Fri Apr 6 2012 Alexander Kurtakov <akurtako@redhat.com> 1.6-1
- Update to latest upstream release.

* Mon Mar 05 2012 Jaromir Capik <jcapik@redhat.com> - 1.5-4
- Migration to plexus-containers-component-metadata

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-2
- Fix depmap macro call

* Tue Nov 1 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5-1
- Update to upstream 1.5 release.

* Thu Jun 9 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4-4
- Build with maven 3.x.
- Use upstream source.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-2
- Add jdependency also to Requires

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.4-1
- Update to 1.4
- Add BR on jdependency >= 0.6
- Add patch to add dependency on maven-artifact-manager

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.3-2
- Replace plexus utils jar with symlink
- Create MAVEN_REPO_LOCAL dir before calling maven

* Tue Jun 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.3-1
- Initial package
