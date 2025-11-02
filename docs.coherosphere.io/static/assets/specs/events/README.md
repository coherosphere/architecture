# Coherosphere Event Schemas (v1)

_Generated: 2025-11-01T11:15:21.292098Z_

These JSON Schemas (Draft 2020-12) define CloudEvents 1.0 envelopes and typed payloads for Coherosphere DDD events.

## Index

| DDD ID | Name | C2 Source | C4 Sequence(s) | File |
|---|---|---|---|---|
| DDD-EVT-01 | MemberRegistered | C2-05 | C4-04 | DDD-EVT-01_MemberRegistered.json |
| DDD-EVT-02 | IdentityVerified | C2-05 | C4-04 | DDD-EVT-02_IdentityVerified.json |
| DDD-EVT-03 | AttestationIssued | C2-05 | C4-04,C4-21 | DDD-EVT-03_AttestationIssued.json |
| DDD-EVT-04 | AttestationRevoked | C2-05 | C4-04,C4-21 | DDD-EVT-04_AttestationRevoked.json |
| DDD-EVT-05 | Event05 | TBD | TBD | DDD-EVT-05_Event05.json |
| DDD-EVT-06 | Event06 | TBD | TBD | DDD-EVT-06_Event06.json |
| DDD-EVT-07 | Event07 | TBD | TBD | DDD-EVT-07_Event07.json |
| DDD-EVT-08 | Event08 | TBD | TBD | DDD-EVT-08_Event08.json |
| DDD-EVT-09 | Event09 | TBD | TBD | DDD-EVT-09_Event09.json |
| DDD-EVT-10 | ImpactScored | C2-01 | C4-01 | DDD-EVT-10_ImpactScored.json |
| DDD-EVT-11 | AlignmentChecked | C2-08 | C4-01,C4-21,C4-06 | DDD-EVT-11_AlignmentChecked.json |
| DDD-EVT-12 | ContributionSubmitted | C2-02 | C4-01 | DDD-EVT-12_ContributionSubmitted.json |
| DDD-EVT-13 | ResonanceUpdated | C2-01 | C4-01,C4-05 | DDD-EVT-13_ResonanceUpdated.json |
| DDD-EVT-14 | CPUpdated | C2-02 | C4-01,C4-05 | DDD-EVT-14_CPUpdated.json |
| DDD-EVT-15 | WeightUpdated | C2-02 | C4-05 | DDD-EVT-15_WeightUpdated.json |
| DDD-EVT-16 | Event16 | TBD | TBD | DDD-EVT-16_Event16.json |
| DDD-EVT-17 | Event17 | TBD | TBD | DDD-EVT-17_Event17.json |
| DDD-EVT-18 | Event18 | TBD | TBD | DDD-EVT-18_Event18.json |
| DDD-EVT-19 | Event19 | TBD | TBD | DDD-EVT-19_Event19.json |
| DDD-EVT-20 | ProposalCreated | C2-03 | C4-02,C4-07 | DDD-EVT-20_ProposalCreated.json |
| DDD-EVT-21 | VoteCast | C2-03 | C4-02 | DDD-EVT-21_VoteCast.json |
| DDD-EVT-22 | VoteTallied | C2-03 | C4-02 | DDD-EVT-22_VoteTallied.json |
| DDD-EVT-23 | DecisionRecorded | C2-03 | C4-02,C4-07 | DDD-EVT-23_DecisionRecorded.json |
| DDD-EVT-24 | PolicyChanged | C2-03 | C4-09,C4-07 | DDD-EVT-24_PolicyChanged.json |
| DDD-EVT-25 | SRIComputed | C2-07 | C4-17,C4-01 | DDD-EVT-25_SRIComputed.json |
| DDD-EVT-26 | KPIUpdated | C2-07 | C4-17,C4-03,C4-01 | DDD-EVT-26_KPIUpdated.json |
| DDD-EVT-27 | FundingAllocated | C2-04 | C4-03 | DDD-EVT-27_FundingAllocated.json |
| DDD-EVT-28 | TreasuryTxPosted | C2-04 | C4-03,C4-10 | DDD-EVT-28_TreasuryTxPosted.json |
| DDD-EVT-29 | RoundOpened | C2-04 | C4-03 | DDD-EVT-29_RoundOpened.json |
| DDD-EVT-30 | RoundClosed | C2-04 | C4-03 | DDD-EVT-30_RoundClosed.json |
| DDD-EVT-31 | DonationRecorded | C2-04 | C4-03 | DDD-EVT-31_DonationRecorded.json |
| DDD-EVT-32 | MatchingComputed | C2-04 | C4-03 | DDD-EVT-32_MatchingComputed.json |
| DDD-EVT-33 | Event33 | TBD | TBD | DDD-EVT-33_Event33.json |
| DDD-EVT-34 | Event34 | TBD | TBD | DDD-EVT-34_Event34.json |
| DDD-EVT-35 | Event35 | TBD | TBD | DDD-EVT-35_Event35.json |
| DDD-EVT-36 | Event36 | TBD | TBD | DDD-EVT-36_Event36.json |
| DDD-EVT-37 | Event37 | TBD | TBD | DDD-EVT-37_Event37.json |
| DDD-EVT-38 | Event38 | TBD | TBD | DDD-EVT-38_Event38.json |
| DDD-EVT-39 | Event39 | TBD | TBD | DDD-EVT-39_Event39.json |
| DDD-EVT-40 | ProjectCreated | C2-06 | C4-14 | DDD-EVT-40_ProjectCreated.json |
| DDD-EVT-41 | MilestoneReported | C2-06 | C4-14 | DDD-EVT-41_MilestoneReported.json |
| DDD-EVT-42 | HubSignal | C2-06 | C4-16 | DDD-EVT-42_HubSignal.json |
| DDD-EVT-43 | ResourceRequest | C2-06 | C4-36,C4-09 | DDD-EVT-43_ResourceRequest.json |
| DDD-EVT-44 | Event44 | TBD | TBD | DDD-EVT-44_Event44.json |
| DDD-EVT-45 | Event45 | TBD | TBD | DDD-EVT-45_Event45.json |
| DDD-EVT-46 | Event46 | TBD | TBD | DDD-EVT-46_Event46.json |
| DDD-EVT-47 | Event47 | TBD | TBD | DDD-EVT-47_Event47.json |
| DDD-EVT-48 | Event48 | TBD | TBD | DDD-EVT-48_Event48.json |
| DDD-EVT-49 | Event49 | TBD | TBD | DDD-EVT-49_Event49.json |
| DDD-EVT-50 | ParamsVersioned | C2-03 | C4-07 | DDD-EVT-50_ParamsVersioned.json |
| DDD-EVT-51 | Event51 | TBD | TBD | DDD-EVT-51_Event51.json |
| DDD-EVT-52 | Event52 | TBD | TBD | DDD-EVT-52_Event52.json |
| DDD-EVT-53 | Event53 | TBD | TBD | DDD-EVT-53_Event53.json |
| DDD-EVT-54 | Event54 | TBD | TBD | DDD-EVT-54_Event54.json |
| DDD-EVT-55 | Event55 | TBD | TBD | DDD-EVT-55_Event55.json |
| DDD-EVT-56 | Event56 | TBD | TBD | DDD-EVT-56_Event56.json |
| DDD-EVT-57 | Event57 | TBD | TBD | DDD-EVT-57_Event57.json |
| DDD-EVT-58 | Event58 | TBD | TBD | DDD-EVT-58_Event58.json |
| DDD-EVT-59 | Event59 | TBD | TBD | DDD-EVT-59_Event59.json |
| DDD-EVT-60 | StreamOpened | C2-04 | C4-10 | DDD-EVT-60_StreamOpened.json |
| DDD-EVT-61 | StreamPaused | C2-04 | C4-10,C4-35 | DDD-EVT-61_StreamPaused.json |
| DDD-EVT-62 | StreamResumed | C2-04 | C4-10,C4-35 | DDD-EVT-62_StreamResumed.json |
| DDD-EVT-63 | StreamClosed | C2-04 | C4-10 | DDD-EVT-63_StreamClosed.json |
| DDD-EVT-64 | Event64 | TBD | TBD | DDD-EVT-64_Event64.json |
| DDD-EVT-65 | Event65 | TBD | TBD | DDD-EVT-65_Event65.json |
| DDD-EVT-66 | Event66 | TBD | TBD | DDD-EVT-66_Event66.json |
| DDD-EVT-67 | Event67 | TBD | TBD | DDD-EVT-67_Event67.json |
| DDD-EVT-68 | Event68 | TBD | TBD | DDD-EVT-68_Event68.json |
| DDD-EVT-69 | Event69 | TBD | TBD | DDD-EVT-69_Event69.json |
| DDD-EVT-70 | IncidentOpened | C2-10 | C4-27,C4-25 | DDD-EVT-70_IncidentOpened.json |
| DDD-EVT-71 | IncidentResolved | C2-10 | C4-27 | DDD-EVT-71_IncidentResolved.json |
| DDD-EVT-72 | TransparencyReportPublished | C2-10 | C4-12,C4-28 | DDD-EVT-72_TransparencyReportPublished.json |
| DDD-EVT-73 | Event73 | TBD | TBD | DDD-EVT-73_Event73.json |
| DDD-EVT-74 | Event74 | TBD | TBD | DDD-EVT-74_Event74.json |
| DDD-EVT-75 | Event75 | TBD | TBD | DDD-EVT-75_Event75.json |
| DDD-EVT-76 | Event76 | TBD | TBD | DDD-EVT-76_Event76.json |
| DDD-EVT-77 | Event77 | TBD | TBD | DDD-EVT-77_Event77.json |
| DDD-EVT-78 | Event78 | TBD | TBD | DDD-EVT-78_Event78.json |
| DDD-EVT-79 | Event79 | TBD | TBD | DDD-EVT-79_Event79.json |
| DDD-EVT-80 | ContractVerified | C2-10 | C4-26 | DDD-EVT-80_ContractVerified.json |
| DDD-EVT-81 | ZkProofPublished | C2-10 | C4-26 | DDD-EVT-81_ZkProofPublished.json |
| DDD-EVT-82 | SystemStressCaptured | C2-10 | C4-29 | DDD-EVT-82_SystemStressCaptured.json |
| DDD-EVT-83 | RiskThresholdBreachDetected | C2-10 | C4-35 | DDD-EVT-83_RiskThresholdBreachDetected.json |
| DDD-EVT-84 | FundingStreamPaused | C2-10 | C4-35 | DDD-EVT-84_FundingStreamPaused.json |
| DDD-EVT-85 | RiskCleared | C2-10 | C4-35 | DDD-EVT-85_RiskCleared.json |
| DDD-EVT-86 | FundingStreamResumed | C2-10 | C4-35 | DDD-EVT-86_FundingStreamResumed.json |
