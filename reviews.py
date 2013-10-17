#!/usr/bin/python
#
# Generate gerrit URLs
#
# See https://review.openstack.org/Documentation/user-search.html for
# docs about available operators.

BASE_URL = "https://review.openstack.org/#/q/%s+(%s),n,z"

FEATURES = [
    "-label:CodeReview=-2",  # Exclude reviews with a -2
    "-label:CodeReview=-1",  # Exclude reviews with a -1
    "status:open",           # Include only open reviews
    "label:Verified=1",      # Include only Jenkins verified reviews
]

PROJECTS = [
    "openstack/tripleo-incubator",
    "openstack/tuskar",
    "openstack/tuskar-ui",
    "openstack-infra/tripleo-ci",
    "openstack/os-apply-config",
    "openstack/os-collect-config",
    "openstack/os-refresh-config",
    "openstack/tripleo-image-elements",
    "openstack/tripleo-heat-templates",
    "openstack/diskimage-builder",
    "openstack/python-tuskarclient"
]


def construct_url():
    """Construct a gerrit URL using global settings"""
    features = "+".join(FEATURES)

    projects = ["project:%s" % project for project in PROJECTS]
    projects = "+OR+".join(projects)
    return BASE_URL % (features, projects)


def main():
    """Main"""
    print(construct_url())

if __name__ == "__main__":
    main()
