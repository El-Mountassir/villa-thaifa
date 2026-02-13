Ce n'étaient pas les seules. Voici d'autres syntaxes qu'on pourrait explorer :

| Syntaxe          | Exemple                 | Origine                            |
| ---------------- | ----------------------- | ---------------------------------- |
| `@name`          | `@evaluations`          | GitHub mentions                    |
| `{{paths.name}}` | `{{paths.evaluations}}` | Jinja/Mustache                     |
| `$NAME`          | `$EVALUATIONS_DIR`      | Shell variables                    |
| `[name]`         | `[evaluations]`         | Markdown references                |
| `%name%`         | `%evaluations%`         | Windows variables                  |
| `:name:`         | `:evaluations:`         | Slack/emoji style                  |
| `~name`          | `~evaluations`          | Home directory style               |
| `path:name`      | `path:evaluations`      | URI scheme style                   |
| `*name`          | `*evaluations`          | YAML anchors                       |
| `[[name]]`       | `[[evaluations]]`       | Wiki-link style (Obsidian, Notion) |
| `${name}`        | `${evaluations}`        | Shell expansion                    |

---

**Question clé** : Qu'est-ce qu'on veut optimiser ?

- Lisibilité en prose ?
- Familiarité pour devs ?
- Pas de collision avec syntaxes existantes ?
- Facilité de parsing (grep, regex) ?
- Support multi-contexte (md, py, bash) ?

On ajoutes ces options au handoff pour le `/think`, ou tu as une intuition sur une direction ?
