domo_bq_map = {
  "Content [C][1] [Latest Metadata]": "c1_content_latest_metadata_vw",
  "Content [C][2] [Structure Metadata]": "c2_content_structure_metadata_vw",
  "Channels [CH][2] [Channel Performance Data Explorer]": "ch2_channel_performance_part2_final_results_vw",
  "1454_CLC [2.0]": "clc_2_0_vw",
  "Glue_Groups [G][2] [Group Users]": "g2_groups_users_vw",
  "Groups [G][3] [Assignment Status]": "g3_groups_assignment_status_vw",
  "Groups [G][3] [Channel Performance Data Explorer]": "g3_groups_channel_performance_vw",
  "Groups [G][3] [Overall Onboarding Status]": "g3_groups_overall_onboarding_status_vw",
  "Groups [G][3] [Group Performance Data Explorer]": "g3_groups_performance_data_explorer_vw",
  "Groups [G][3] [Search User Details]": "g3_groups_search_user_details_vw",
  "Groups [G][3] [Skills & Learning Goals]": "g3_groups_skills_learninggoals_vw",
  "Groups [G][3] [Structured Content Performance Data Explorer]": "g3_groups_structured_content_performance_data_explorer_vw",
  "Groups [G][3] [Structured Journey Progression Data Explorer]": "g3_groups_structured_journey_progression_data_explorer_vw",
  "Groups [G][4] [Structured Journey Progression Overview]": "g4_groups_structured_journey_progression_overview_vw",
  "Groups [G][4] [Structured Pathway Progression Overview]": "g4_groups_structured_pathway_progression_overview_vw",
  "Groups [G][3] [Structured Pathway Progression Data Explorer]": "g3_groups_structured_pathway_progression_data_explorer_vw",
  "LeaderBoard_Data": "leaderboard_data_part2_final_vw",
  "LeaderBoard User Agg Score": "leaderboard_user_agg_score_vw",
  "Searches [SE][1] [Search User Details]": "se1_searches_search_user_details",
  "Glue Users [U][1] [Live Event Cards]": "u1_users_live_event_cards_vw",
  "Glue Users [U][1] [Project Cards]": "u1_users_project_cards_vw",
  "Skills_ Users [U][1]": "u1_users_skills_vw",
  "Quiz[U][2][Data Explorer]": "u2_quiz_data_explorer_part3_final_vw",
  "Users [U][2] [Assignment Status]": "u2_users_assignment_status_vw",
  "Users [U][2][LXP roles]": "u2_users_lxp_roles_vw",
  "Users [U][2] [User Performance Data Explorer]": "u2_users_performance_part5_final_results_vw",
  "Glue Users [U][2] [Quiz & Poll Responses]": "u2_users_quiz_and_poll_responses_vw",
  "Users [U][2][Scorm Data Explorer]": "u2_users_scorm_data_explorer_vw",
  "Users [U][2][Skill and Learning goals]": "u2_users_skills_learninggoals_vw",
  "Users [U][3] [Overall Onboarding Status]": "u3_overall_onboarding_status_part4_final_vw",
  "User[U][3] Adoption_Details": "u3_users_adoption_details_vw",
  "Users [U][3][User Funnel Data Explorer]": "u3_users_user_funnel_data_explorer_vw",
  "Glue_Users [U][3] [Structured Content Performance Data Explorer]": "u3_users_structured_content_performance_data_explorer_vw",
  "UserCards [U][0] [Core Event Data - Buffered]": "u0_usercards_event_vw",
  "Glue_Users [U][1] [Latest Metadata]": "u1_users_latest_metadata_vw"
}

looker_tables_analysis = ['c1_content_latest_metadata_vw',
 'c2_content_structure_metadata_vw',
 'ch2_channel_performance_part2_final_results_vw',
 'clc_2_0_vw',
 'g2_groups_users_vw',
 'g3_groups_assignment_status_vw',
 'g3_groups_channel_performance_vw',
 'g3_groups_overall_onboarding_status_vw',
 'g3_groups_performance_data_explorer_vw',
 'g3_groups_search_user_details_vw',
 'g3_groups_skills_learninggoals_vw',
 'g3_groups_structured_content_performance_data_explorer_vw',
 'g3_groups_structured_journey_progression_data_explorer_vw',
 'g4_groups_structured_journey_progression_overview_vw',
 'g4_groups_structured_pathway_progression_overview_vw',
 'g3_groups_structured_pathway_progression_data_explorer_vw',
 'leaderboard_data_part2_final_vw',
 'leaderboard_user_agg_score_vw',
 'se1_searches_search_user_details_vw',
 'u1_users_live_event_cards_vw',
 'u1_users_project_cards_vw',
 'u1_users_skills_vw',
 'u2_quiz_data_explorer_part3_final_vw',
 'u2_users_assignment_status_vw',
 'u2_users_lxp_roles_vw',
 'u2_users_performance_part5_final_results_vw',
 'u2_users_quiz_and_poll_responses_vw',
 'u2_users_scorm_data_explorer_vw',
 'u2_users_skills_learninggoals_vw',
 'u3_overall_onboarding_status_part4_final_vw',
 'u3_users_adoption_details_vw',
 'u3_users_user_funnel_data_explorer_vw',
 'u3_users_structured_content_performance_data_explorer_vw',
 'u0_usercards_event_vw',
 'u1_users_latest_metadata_vw']

looker_table_columns ={'c1_content_latest_metadata_vw': ['card_id',
  'current_content_owner_full_name',
  'card_state',
  'card_subtype',
  'card_type',
  'ecl_id',
  'ecl_source_name',
  'is_public',
  'duration_hhmm',
  'duration',
  'duration_seconds',
  'published_at',
  'card_title',
  'created_at',
  'updated_at',
  'card_level',
  'average_rating',
  'standard_card_type',
  'content_structure',
  'author_id',
  'card_author_full_name',
  'external_id',
  'card_languages',
  'tags'],
 'c2_content_structure_metadata_vw': ['pathway_id',
  'card_id',
  'card_type',
  'pathway_state',
  'pathway_title',
  'channel_id',
  'channel_name',
  'carousel_name',
  'overall_content_structure',
  'journey_id',
  'journey_title',
  'journey_pathway_id',
  'journey_pathway_title',
  'journey_state',
  'card_state',
  'channel_content',
  'journey_content',
  'pathway_content',
  'journey_pathway_content',
  'carousel_content',
  'card_author_id',
  'card_author_full_name',
  'card_title',
  'card_resource_url',
  'card_subtype',
  'ecl_source_name',
  'is_public',
  'duration_hhmm',
  'duration_seconds',
  'standard_card_type',
  'card_level',
  'average_rating'],
 'ch2_channel_performance_part2_final_results_vw': ['user_id',
  'user_full_name',
  'email',
  'time',
  'channel_id',
  'platform',
  'performance_metric',
  'event',
  'channel_name',
  'channel_status',
  'user_account_status',
  'excluded_from_leaderboard',
  'is_channel_private',
  'is_ecl_enabled',
  'is_channel_curated'],
 'clc_2_0_vw': ['id',
  'entity_id',
  'entity_type',
  'from_date',
  'to_date',
  'target_score',
  'target_steps',
  'deleted_at',
  'created_at',
  'updated_at',
  'name',
  'status',
  'org_id_s',
  'user_id',
  'user_full_name',
  'user_account_status',
  'excluded_from_leaderboard',
  'email',
  'time_account_created',
  'completable_id',
  'completed_at',
  'completed_percentage',
  'duration',
  'external_id',
  'card_id',
  'card_type',
  'completion_language',
  'manager',
  'manager_email',
  'occurences',
  'clcstatus',
  'clc_name',
  'record_insert_time',
  'etl_record_created_time',
  'tags'],
 'g2_groups_users_vw': ['user_id',
  'group_id',
  'group_name',
  'group_user_role',
  'group_status'],
 'g3_groups_assignment_status_vw': ['user_full_name',
  'user_id',
  'email',
  'assignment_state',
  'time_assignment_started',
  'time_completed',
  'assignment_due_date',
  'card_id',
  'card_state',
  'card_title',
  'card_type',
  'is_user_generated',
  'content_structure',
  'content_status',
  'assignor_full_name',
  'assignor_id',
  'group_id',
  'assignment_type',
  'assignment_progression',
  'group_name',
  'group_status',
  'user_account_status',
  'excluded_from_leaderboard',
  'card_subtype',
  'ecl_source_name',
  'is_public',
  'duration_seconds',
  'duration_hhmm',
  'group_assignment_association',
  'card_level',
  'average_rating',
  'standard_card_type',
  'assigned_date'],
 'g3_groups_channel_performance_vw': ['user_id',
  'user_full_name',
  'email',
  'time',
  'channel_id',
  'platform',
  'performance_metric',
  'event',
  'group_id',
  'group_name',
  'group_status',
  'group_user_role',
  'user_account_status',
  'excluded_from_leaderboard',
  'is_channel_private',
  'channel_status',
  'channel_name',
  'is_ecl_enabled',
  'is_channel_curated',
  'external_id',
  'manager',
  'manager_email',
  'etl_record_created_time'],
 'g3_groups_overall_onboarding_status_vw': ['user_id',
  'user_full_name',
  'email',
  'time_account_created',
  'sign_in_count',
  'user_account_status',
  'excluded_from_leaderboard',
  'latest_day_of_active_engagement',
  'total_days_of_active_engagement',
  'first_day_of_active_engagement',
  'overall_onboarding_status',
  'group_id',
  'time_account_suspended',
  'group_name',
  'group_status',
  'group_user_role',
  'external_id',
  'parsed_first_day_of_active_engagement',
  'parsed_latest_day_of_active_engagement'],
 'g3_groups_performance_data_explorer_vw': ['user_id',
  'group_id',
  'group_name',
  'group_status',
  'card_id',
  'card_state',
  'card_title',
  'card_type',
  'content_structure',
  'card_author_id',
  'user_full_name',
  'email',
  'time',
  'event',
  'shared_to_user_id',
  'shared_to_group_id',
  'platform',
  'performance_metric',
  'time_account_created',
  'sign_in_count',
  'user_account_status',
  'excluded_from_leaderboard',
  'duration_seconds',
  'duration_hhmm',
  'ecl_source_name',
  'card_subtype',
  'card_resource_url',
  'is_public',
  'assigned_content',
  'standard_card_type',
  'published_at',
  'card_rating',
  'time_account_suspended',
  'content_completion_sync',
  'card_level',
  'average_rating'],
 'g3_groups_search_user_details_vw': ['time',
  'analytics_version',
  'event',
  'is_admin_request',
  'is_system_generated',
  'hostname',
  'org_id',
  'platform',
  'platform_version_number',
  'results_count',
  'search_query',
  'user_agent',
  'user_id',
  'user_full_name',
  'email',
  'time_account_created',
  'user_account_status',
  'group_id',
  'group_name',
  'group_status',
  'group_user_role',
  'excluded_from_leaderboard',
  'external_id'],
 'g3_groups_skills_learninggoals_vw': ['user_id',
  'user_full_name',
  'email',
  'time_account_created',
  'user_account_status',
  'time',
  'event',
  'topic_type',
  'topic_label',
  'group_id',
  'group_name',
  'group_status',
  'group_user_role',
  'excluded_from_leaderboard',
  'external_id',
  'sign_in_count',
  'time_account_suspended',
  'manager',
  'manager_email',
  'etl_record_created_time'],
 'g3_groups_structured_content_performance_data_explorer_vw': ['pathway_id',
  'card_id',
  'card_type',
  'card_title',
  'pathway_state',
  'pathway_title',
  'channel_id',
  'channel_name',
  'carousel_name',
  'journey_id',
  'journey_title',
  'journey_pathway_id',
  'journey_pathway_title',
  'journey_state',
  'card_state',
  'channel_content',
  'journey_content',
  'pathway_content',
  'carousel_content',
  'user_id',
  'user_full_name',
  'email',
  'time',
  'platform',
  'performance_metric',
  'group_name',
  'group_status',
  'content_structure',
  'excluded_from_leaderboard',
  'time_account_created',
  'assigned_content',
  'user_account_status',
  'card_subtype',
  'ecl_source_name',
  'is_public',
  'standard_card_type',
  'duration_seconds',
  'duration_hhmm'],
 'g3_groups_structured_journey_progression_data_explorer_vw': ['group_id',
  'group_name',
  'group_status',
  'content_structure',
  'journey_id',
  'journey_title',
  'journey_pathway_id',
  'journey_pathway_title',
  'card_id',
  'card_title',
  'card_type',
  'user_id',
  'time_completed',
  'user_full_name',
  'email',
  'journey_content',
  'pathway_content',
  'journey_pathway_content',
  'channel_id',
  'channel_name',
  'carousel_name',
  'journey_state',
  'card_author_full_name',
  'card_author_id',
  'card_state',
  'overall_content_structure',
  'excluded_from_leaderboard',
  'user_account_status',
  'duration_seconds',
  'duration_hhmm',
  'card_subtype',
  'ecl_source_name',
  'card_level',
  'completed_percentage'],
 'g4_groups_structured_journey_progression_overview_vw': ['group_id',
  'group_name',
  'group_status',
  'group_user_role',
  'user_id',
  'journey_id',
  'journey_title',
  'journey_pathway_id',
  'journey_pathway_title',
  'content_structure',
  'total_cards_completed',
  'overall_completion_status',
  'user_full_name',
  'email',
  'journey_pathway_progress',
  'total_journey_cards',
  'time_completed',
  'journey_completion_progress',
  'journey_pathway_completion_progress',
  'journey_pathway_completion_status',
  'channel_id',
  'channel_name',
  'carousel_name',
  'channel_content',
  'carousel_content',
  'journey_content',
  'pathway_content',
  'ecl_source_name',
  'is_public',
  'excluded_from_leaderboard',
  'user_account_status',
  'card_state',],
 'g4_groups_structured_pathway_progression_overview_vw': ['group_id',
  'group_name',
  'group_status',
  'user_id',
  'total_pathway_child_cards',
  'content_structure',
  'total_cards_completed',
  'pathway_progress',
  'overall_completion_status',
  'time_completed',
  'user_full_name',
  'email',
  'pathway_id',
  'pathway_title',
  'completion_progress',
  'channel_id',
  'channel_name',
  'carousel_name',
  'channel_content',
  'carousel_content',
  'journey_content',
  'pathway_content',
  'pathway_state',
  'card_author_full_name',
  'card_author_id',
  'time_account_created',
  'user_account_status',
  'excluded_from_leaderboard',
  'pathway_progress_seconds'],
 'g3_groups_structured_pathway_progression_data_explorer_vw': ['group_id',
  'group_name',
  'content_structure',
  'pathway_id',
  'pathway_title',
  'card_id',
  'card_title',
  'card_type',
  'user_id',
  'time_completed',
  'user_full_name',
  'email',
  'journey_content',
  'pathway_content',
  'journey_pathway_content',
  'channel_id',
  'channel_name',
  'carousel_name',
  'channel_content',
  'carousel_content',
  'pathway_state',
  'card_state',
  'overall_content_structure',
  'excluded_from_leaderboard',
  'user_account_status',
  'duration_seconds',
  'duration_hhmm',
  'card_resource_url',
  'card_subtype',
  'ecl_source_name',
  'card_level',
  'average_rating',
  'completed_percentage',
  'manager_email',
  'manager'],
 'leaderboard_data_part2_final_vw': ['user_id',
  'score',
  'date',
  'score_total',
  'skill',
  'user_skills_combined',
  'user_skills_distinct_count',
  'group_name',
  'group_user_role',
  'user_group_combined',
  'user_group_distinct_count',
  'user_full_name',
  'user_account_status',
  'excluded_from_leaderboard',
  'email'],
 'leaderboard_user_agg_score_vw': ['score_total',
  'user_id',
  'user_full_name',
  'user_account_status',
  'excluded_from_leaderboard'],
 'se1_searches_search_user_details_vw': ['time',
  'analytics_version',
  'event',
  'is_admin_request',
  'is_system_generated',
  'hostname',
  'org_id',
  'platform',
  'platform_version_number',
  'results_count',
  'search_query',
  'user_agent',
  'user_id',
  'user_full_name',
  'email',
  'time_account_created',
  'sign_in_count',
  'user_account_status',
  'excluded_from_leaderboard',
  'external_id',
  'manager',
  'manager_email',
  'etl_record_created_time'],
 'u1_users_live_event_cards_vw': ['time',
  'training_end_date',
  'training_start_date',
  'training_registration_id',
  'training_registration_state',
  'event',
  'card_id',
  'user_id',
  'card_resource_url',
  'card_state',
  'card_subtype',
  'card_title',
  'card_type',
  'ecl_id',
  'ecl_source_name',
  'is_public',
  'content_structure',
  'user_full_name',
  'email',
  'excluded_from_leaderboard',
  'registration_limit',
  'registration_type',
  'time_zone',
  'last_registration_date',
  'card_level',
  'average_rating',
  'standard_card_type',
  'published_at',
  'external_id',
  'current_content_owner_full_name',
  'card_languages',
  'is_card_promoted',
  'etl_record_created_time',
  'tags'],
 'u1_users_project_cards_vw': ['time',
  'card_id',
  'event',
  'grade_range',
  'grader_type',
  'grading_system',
  'project_card_submission_id',
  'submitter_type',
  'submission_status',
  'grade',
  'card_resource_url',
  'card_state',
  'card_subtype',
  'card_title',
  'card_type',
  'ecl_id',
  'ecl_source_name',
  'is_public',
  'content_structure',
  'card_author_id',
  'card_author_full_name',
  'submitter_full_name',
  'email',
  'time_account_created',
  'sign_in_count',
  'user_account_status',
  'excluded_from_leaderboard',
  'manager',
  'manager_email',
  'grader_full_name',
  'project_card_submission_url',
  'card_level',
  'average_rating',
  'standard_card_type',
  'published_at',
  'external_id'],
 'u1_users_skills_vw': ['skill_id',
  'user_id',
  'created_at',
  'experience',
  'skill_level',
  'skill_type',
  'skill_name',
  'user_full_name',
  'user_account_status',
  'excluded_from_leaderboard',
  'email',
  'time_account_created',
  'sign_in_count',
  'time_account_suspended',
  'external_id',
  'manager',
  'manager_email',
  'credential_name',
  'etl_record_created_time'],
 'u2_quiz_data_explorer_part3_final_vw': ['time',
  'card_id',
  'event',
  'quiz_option_id',
  'quiz_reanswerable',
  'quiz_option_label',
  'quiz_attempt_id',
  'quiz_attempt_passed',
  'quiz_option_is_correct',
  'quiz_id',
  'quiz_question_id',
  'user_id',
  'card_resource_url',
  'card_state',
  'card_subtype',
  'card_title',
  'card_type',
  'is_public',
  'content_structure',
  'card_author_id',
  'card_author_full_name',
  'user_full_name',
  'email',
  'time_account_created',
  'user_account_status',
  'excluded_from_leaderboard',
  'quiz_question_label',
  'quiz_passing_criteria',
  'total_quiz_attempts',
  'quiz_questions_passed',
  'card_level',
  'average_rating',
  'published_at',
  'standard_card_type',
  'external_id',
  'current_content_owner_full_name'],
 'u2_users_assignment_status_vw': ['user_full_name',
  'user_id',
  'email',
  'assignment_state',
  'time_assignment_started',
  'time_completed',
  'assignment_due_date',
  'time_assignment_created',
  'card_id',
  'card_state',
  'card_title',
  'card_type',
  'content_structure',
  'card_subtype',
  'ecl_id',
  'ecl_source_name',
  'is_public',
  'duration_seconds',
  'duration_hhmm',
  'user_account_status',
  'excluded_from_leaderboard',
  'card_level',
  'average_rating',
  'standard_card_type',
  'published_at',
  'external_id',
  'assigned_date',
  'card_languages',
  'assignment_type',
  'assignor_full_name',
  'assignment_progression'],
 'u2_users_lxp_roles_vw': ['user_full_name',
  'user_account_status',
  'excluded_from_leaderboard',
  'email',
  'time_account_created',
  'sign_in_count',
  'time_account_suspended',
  'external_id',
  'manager',
  'manager_email',
  'lxp_role',
  'user_id',
  'role_id',
  'lxp_role_new'],
 'u2_users_performance_part5_final_results_vw': ['card_id',
  'card_state',
  'card_title',
  'card_type',
  'content_structure',
  'author_id',
  'card_author_id',
  'user_id',
  'user_full_name',
  'email',
  'time',
  'event',
  'shared_to_user_id',
  'shared_to_group_id',
  'platform',
  'performance_metric',
  'time_account_created',
  'sign_in_count',
  'user_account_status',
  'excluded_from_leaderboard',
  'card_resource_url',
  'duration_seconds',
  'duration_hhmm',
  'ecl_id',
  'ecl_source_name',
  'is_public',
  'card_subtype',
  'assigned_content',
  'standard_card_type',
  'time_account_suspended',
  'content_completion_sync',],
 'u2_users_quiz_and_poll_responses_vw': ['time',
  'user_id',
  'card_id',
  'event',
  'card_type',
  'response',
  'poll_option_id',
  'quiz_option_id',
  'response_type',
  'total_responses',
  'user_full_name',
  'email',
  'time_account_created',
  'user_account_status',
  'excluded_from_leaderboard',
  'is_correct',
  'card_resource_url',
  'card_state',
  'card_subtype',
  'card_title',
  'ecl_source_name',
  'is_public',
  'content_structure',
  'card_author_id',
  'card_author_full_name',
  'card_level',
  'average_rating',
  'standard_card_type',
  'published_at',
  'current_content_owner_full_name',
  'card_languages',
  'p_week',
  'tags'],
 'u2_users_scorm_data_explorer_vw': ['time',
  'card_id',
  'event',
  'user_id',
  'scorm_attempts',
  'scorm_course_id',
  'scorm_registration_success',
  'scorm_score',
  'scorm_total_seconds_tracked',
  'scorm_registration_status',
  'performance_metric',
  'user_full_name',
  'user_account_status',
  'excluded_from_leaderboard',
  'email',
  'time_account_created',
  'card_state',
  'card_title',
  'card_type',
  'content_structure',
  'card_author_id',
  'card_author_full_name',
  'card_resource_url',
  'card_subtype',
  'ecl_id',
  'ecl_source_name',
  'is_public',
  'duration_seconds',
  'duration_hhmm',
  'card_level',
  'average_rating',
  'standard_card_type',
  'published_at',
  'external_id'],
 'u2_users_skills_learninggoals_vw': ['user_id',
  'user_full_name',
  'email',
  'time_account_created',
  'user_account_status',
  'time',
  'event',
  'topic_type',
  'topic_label',
  'excluded_from_leaderboard',
  'external_id',
  'manager',
  'manager_email',
  'sign_in_count',
  'time_account_suspended',
  'topic_id',
  'topic_label_1',
  'etl_record_created_time'],
 'u3_overall_onboarding_status_part4_final_vw': ['user_id',
  'user_full_name',
  'email',
  'time_account_created',
  'sign_in_count',
  'user_account_status',
  'excluded_from_leaderboard',
  'manager',
  'manager_email',
  'latest_day_of_active_engagement',
  'total_days_of_active_engagement',
  'first_day_of_active_engagement',
  'time_of_first_session',
  'time_of_last_session',
  'total_sessions',
  'external_id',
  'time_account_suspended',
  'p_year',
  'etl_record_created_time',
  'parsed_first_day_of_active_engagement',
  'parsed_latest_day_of_active_engagement',
  'overall_onboarding_status'],
 'u3_users_adoption_details_vw': ['user_id',
  'time',
  'adoption_metric',
  'user_full_name',
  'user_account_status',
  'excluded_from_leaderboard',
  'email',
  'time_account_created',
  'sign_in_count',
  'time_account_suspended',
  'external_id'],
 'u3_users_user_funnel_data_explorer_vw': ['user_id',
  'metrics',
  'email',
  'user_account_status',
  'user_full_name',
  'etl_record_created_time'],
 'u3_users_structured_content_performance_data_explorer_vw': ['pathway_id',
  'card_id',
  'card_type',
  'pathway_state',
  'card_title',
  'pathway_title',
  'channel_name',
  'carousel_name',
  'journey_id',
  'journey_title',
  'journey_pathway_id',
  'journey_pathway_title',
  'journey_state',
  'card_state',
  'channel_content',
  'journey_content',
  'pathway_content',
  'journey_pathway_content',
  'user_id',
  'user_full_name',
  'email',
  'time',
  'performance_metric',
  'content_structure',
  'excluded_from_leaderboard',
  'time_account_created',
  'user_account_status',
  'card_subtype',
  'ecl_source_name',
  'card_level',
  'duration_seconds',
  'standard_card_type',
  'duration_hhmm'],
 'u0_usercards_event_vw': ['time',
  'card_id',
  'card_author_id',
  'event',
  'user_id',
  'platform',
  'shared_to_user_id',
  'is_user_generated',
  'channel_id',
  'assigned_to_user_id',
  'channel_follower_id',
  'topic_label',
  'topic_name',
  'pathway_id',
  'pathway_name',
  'journey_id',
  'journey_name',
  'group_user_role',
  'card_subtype',
  'card_resource_url',
  'ecl_id',
  'card_duration',
  'badge_title',
  'completion_type',
  'onboarding_status',
  'scorm_user_id',
  'skill_id',
  'skill_name',
  'job_family',
  'job_role',
  'skill_category',
  'skill_level_rated',
  'occupation_id',
  'occupation_name',
  'occupation_category',
  'edited_user_id',
  'is_open_source_content',
  'external_id',
  'channel_card_user_id',
  'assigned_to_user_organization_role',
  'group_user_first_name',
  'group_user_last_name',
  'group_user_email',
  'group_user_handle',
  'group_user_organization_role',
  'user_first_name',
  'user_last_name',
  'user_organization_role',
  'user_email',
  'user_last_sign_in_at',
  'user_handle',
  'user_exclude_from_leaderboard',
  'user_created_at',
  'user_status',
  'user_sign_in_count',
  'user_name',
  'duration',
  'title',
  'card_message',
  'card_type',
  'standard_type',
  'card_level',
  'card_source_name',
  'card_created_at',
  'card_is_public',
  'readable_card_type',],
 'u1_users_latest_metadata_vw': ['user_id',
  'user_full_name',
  'user_account_status',
  'excluded_from_leaderboard',
  'email',
  'time_account_created',
  'sign_in_count',
  'time_account_suspended']}

