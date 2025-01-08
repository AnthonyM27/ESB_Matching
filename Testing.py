#Testing
from ESB_Matching import ESB_Matching
tester = ESB_Matching()

def test_stable_matching():
    #Engineer preferences from greatest interest to least.
    engineer_prefs = [
        [0, 1, 2, 3],  #Engineer 0 prefers project 0 > 1 > 2 > 3
        [1, 0, 3, 2],  
        [2, 3, 0, 1],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [1, 3, 2, 0],
        [2, 0, 3, 1],
        [3, 1, 0, 2],
        [0, 1, 3, 2],
        [1, 2, 0, 3],
        [2, 3, 1, 0],
        [3, 0, 2, 1],
        [0, 2, 3, 1],
        [1, 3, 0, 2],
        [2, 0, 1, 3],
        [3, 1, 2, 0],
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
        ]
    project_prefs = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],  #Project 0
        [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],  #Project 1
        [2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 16, 17],  #Project 2
        [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12, 19, 18, 17, 16]   #Project 3
    ]
    num_projects = 4
    engineers_per_project = 5

    #Apply the stable matching algorithm
    result = tester.stable_matching(engineer_prefs, project_prefs, num_projects, engineers_per_project)

    #Project size validation
    assert all(len(engineers) == engineers_per_project for engineers in result.values()), "Projects do not have correct team sizes."

    #Uniqueness validation
    all_assigned = [engineer for engineers in result.values() for engineer in engineers]
    assert len(all_assigned) == len(set(all_assigned)) == len(engineer_prefs), "Engineers are not uniquely assigned."
    
    #Stable pairing validation
    for project, engineers in result.items():
        for engineer in engineers:
            engineer_pref_list = engineer_prefs[engineer]
            project_pref_list = project_prefs[project]

            # Engineers ranked projects more preferred than the current one
            better_projects = engineer_pref_list[:engineer_pref_list.index(project)]
            for better_project in better_projects:
                engineers_in_better_project = result[better_project]
                if engineer in project_prefs[better_project]:
                    better_project_rank = project_prefs[better_project].index(engineer)
                    worst_current_in_project = max(
                        engineers_in_better_project,
                        key=lambda e: project_prefs[better_project].index(e)
                    )
                    if better_project_rank < project_prefs[better_project].index(worst_current_in_project):
                        assert False, "Matching is not stable."

    print("All tests passed!")

test_stable_matching()