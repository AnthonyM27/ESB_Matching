#ESB_Matching
class ESB_Matching:
    # Input: engineer_prefs (list of lists), project_prefs (list of lists), num_projects, engineers_per_project
    def stable_matching(self, engineer_prefs, project_prefs, num_projects, engineers_per_project):
        """Generate a stable matching of engineers to projects.
        
        Args:
            engineer_prefs (list of lists): project preferences for engineers.
            project_prefs (list of lists): engineer preferences for projects.
            num_projects (int): number of projects.
            engineers_per_project (int): number of engineers to be on each project.

        Returns:
            list of lists: The engineers that are to be put on each project.
        """
        unassigned_engineers = list(range(len(engineer_prefs)))
        project_slots = {ind: [] for ind in range(num_projects)}

        while unassigned_engineers:
            engineer = unassigned_engineers.pop(0)
            for project in engineer_prefs[engineer]:
                if len(project_slots[project]) < engineers_per_project:
                    project_slots[project].append(engineer)
                    break
                else:
                    worst_engineer = get_worst_engineer(project, project_slots, project_prefs)
                    if is_better_choice(engineer, worst_engineer, project_prefs):
                        project_slots[project].remove(worst_engineer)
                        unassigned_engineers.append(worst_engineer)
                        project_slots[project].append(engineer)
                        break
        return project_slots
    
    def get_worst_engineer(project, project_slots, project_prefs):
        """
        Find the worst-ranked engineer currently assigned to a project.

        Args:
            project (int): The project ID.
            project_slots (dict): Dictionary mapping project IDs to their current list of assigned engineers.
            project_prefs (list): List of lists representing project preferences.

        Returns:
            int: The engineer ID ranked worst among the current assignments.
        """
        current_engineers = project_slots[project]
        project_ranking = project_prefs[project]

        # Sort current engineers by their rank in the project's preference list
        worst_engineer = max(current_engineers, key=lambda engineer: project_ranking.index(engineer))
        return worst_engineer

    def is_better_choice(new_engineer, current_engineer, project_prefs):
        """
        Check if a new engineer is a better choice for a project than a currently assigned engineer.

        Args:
            new_engineer (int): The ID of the new engineer proposing.
            current_engineer (int): The ID of the currently assigned engineer.
            project_prefs (list): List of lists representing project preferences.

        Returns:
            bool: True if the new engineer is a better choice, False otherwise.
        """
        project_ranking = project_prefs

        # Compare the rank of the new engineer and the current engineer
        return project_ranking.index(new_engineer) < project_ranking.index(current_engineer)