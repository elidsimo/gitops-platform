# Plateforme GitOps + DevSecOps + Observabilité

Projet de démonstration d'une chaîne de livraison moderne, automatisée et sécurisée.

## Objectifs

- **GitOps** : ArgoCD synchronise le cluster depuis ce dépôt (pattern app of apps)
- **DevSecOps** : Trivy, SonarQube, Gitleaks, Checkov/tfsec dans le pipeline CI
- **Observabilité** : Prometheus, Grafana, Loki, OpenTelemetry + Tempo
- **SRE** : SLO/SLI, alertes Alertmanager, runbooks
- **Bonus** : déploiement progressif (Argo Rollouts) et test de chaos

## Structure du dépôt

| Dossier | Rôle |
|---|---|
| `cluster/` | Configuration du cluster local et bootstrap ArgoCD |
| `apps/` | Applications gérées par ArgoCD |
| `infra/terraform/` | Infrastructure as Code |
| `app-demo/` | Application de démonstration |
| `docs/runbooks/` | Runbooks d'exploitation |
| `.github/workflows/` | Pipelines CI/CD |

## Avancement

- [x] Phase 1 : initialisation du projet et du cluster local
- [x] Phase 2 : ArgoCD et pattern app of apps
- [x] Phase 3 : pipeline DevSecOps, partie 1 (Gitleaks + Trivy)
- [x] Phase 4 : durcissement Kubernetes (securityContext) et Trivy bloquant
